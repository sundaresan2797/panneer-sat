import json
import logging
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app.config import get_settings
from app.schemas.enquiry import EnquiryIn
from app.schemas.sagbs import SAGBSEnquiryIn

logger = logging.getLogger("sat.sheets")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Column order written to the sheet — add a matching header row once, by hand,
# in this exact order (see BUSINESS_DETAILS_TO_CONFIRM.md).
COLUMNS = [
    "Submitted At", "Name", "Company", "Phone", "Email",
    "Location", "Service", "Workers / Vehicles", "Requirement", "Language",
]


SAGBS_TAB = "Sheet2"
SAGBS_COLUMNS = [
    "Submitted At", "Reference", "Name", "Company", "Phone", "Email",
    "Country", "Service", "Engagement", "Budget", "Message", "Consent",
]


def _get_credentials():
    settings = get_settings()

    if settings.google_service_account_json:
        info = json.loads(settings.google_service_account_json)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)

    if settings.google_application_credentials:
        return service_account.Credentials.from_service_account_file(
            settings.google_application_credentials, scopes=SCOPES
        )

    return None


def append_enquiry_to_sheet(enquiry: EnquiryIn) -> bool:
    """Append the enquiry as a new row in the configured Google Sheet.
    Returns False (never raises) if Sheets isn't configured or the API call
    fails, so a Sheets outage never blocks the enquiry response."""
    settings = get_settings()

    row = [
        _submitted_at(), enquiry.name, enquiry.company_name or "", enquiry.phone,
        enquiry.email or "", enquiry.location, enquiry.service,
        enquiry.workers_or_vehicles or "", enquiry.message, enquiry.language,
    ]
    return _append_row(settings.google_sheet_id, settings.google_sheet_tab, row, "USER_ENTERED")


def _submitted_at(timestamp=None):
    timestamp = timestamp or datetime.now(timezone.utc)
    if timestamp.tzinfo is None:  # SQLite returns the stored UTC time without a timezone.
        timestamp = timestamp.replace(tzinfo=timezone.utc)
    return timestamp.astimezone(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")


def append_sagbs_contact_to_sheet(enquiry: SAGBSEnquiryIn, reference: str, *, saved_at=None) -> bool:
    settings = get_settings()
    row = [
        _submitted_at(saved_at), reference, enquiry.name, enquiry.company_name, enquiry.phone,
        enquiry.email, enquiry.country, enquiry.service, enquiry.engagement,
        enquiry.budget, enquiry.message, enquiry.consent,
    ]
    if settings.google_sheet_tab.casefold() == SAGBS_TAB.casefold():
        logger.error("SAT already uses Sheet2; cannot use it for SAGBS contacts.")
        return False
    return _append_row(settings.google_sheet_id, SAGBS_TAB, row, "RAW", ensure_sagbs_tab=True, existing_reference=reference if saved_at else None)


def _prepare_sagbs_tab(sheets, sheet_id):
    def tab_exists():
        metadata = sheets.get(spreadsheetId=sheet_id, fields="sheets(properties(title))").execute()
        return any(sheet["properties"]["title"] == SAGBS_TAB for sheet in metadata["sheets"])

    if not tab_exists():
        try:
            sheets.batchUpdate(spreadsheetId=sheet_id, body={"requests": [
                {"addSheet": {"properties": {"title": SAGBS_TAB}}}
            ]}).execute()
        except HttpError as exc:
            # Another submission may have created the tab concurrently.
            if exc.resp.status != 400 or not tab_exists():
                raise

    header_range = f"'{SAGBS_TAB}'!A1:L1"
    values = sheets.values()
    header = values.get(spreadsheetId=sheet_id, range=header_range).execute()
    if not header.get("values"):
        values.update(spreadsheetId=sheet_id, range=header_range, valueInputOption="RAW",
                      body={"values": [SAGBS_COLUMNS]}).execute()


def _append_row(sheet_id, tab, row, input_option, *, ensure_sagbs_tab=False, existing_reference=None):
    if not sheet_id:
        logger.warning("GOOGLE_SHEET_ID is missing; skipping sheet log.")
        return False
    try:
        credentials = _get_credentials()
        if credentials is None:
            logger.warning("Google Sheets credentials missing; skipping sheet log.")
            return False
        service = build("sheets", "v4", credentials=credentials, cache_discovery=False)
        sheets = service.spreadsheets()
        if ensure_sagbs_tab:
            _prepare_sagbs_tab(sheets, sheet_id)
            if existing_reference:
                references = sheets.values().get(spreadsheetId=sheet_id, range="'Sheet2'!B2:B").execute()
                if [existing_reference] in references.get("values", []):
                    return True
        escaped_tab = tab.replace("'", "''")
        sheets.values().append(
            spreadsheetId=sheet_id,
            range=f"'{escaped_tab}'!A1",
            valueInputOption=input_option,
            insertDataOption="INSERT_ROWS",
            body={"values": [row]},
        ).execute()
        return True
    except FileNotFoundError:
        logger.error("Google credential file missing. Check GOOGLE_APPLICATION_CREDENTIALS.")
        return False
    except HttpError:
        logger.exception("Google Sheets API rejected the append (check sharing / sheet id / tab name)")
        return False
    except Exception:
        logger.exception("Failed to append enquiry to Google Sheets")
        return False
