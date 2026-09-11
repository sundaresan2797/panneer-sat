import json
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app.config import get_settings
from app.schemas.enquiry import EnquiryIn

logger = logging.getLogger("sat.sheets")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Column order written to the sheet — add a matching header row once, by hand,
# in this exact order (see BUSINESS_DETAILS_TO_CONFIRM.md).
COLUMNS = [
    "Submitted At", "Name", "Company", "Phone", "Email",
    "Location", "Service", "Workers / Vehicles", "Requirement", "Language",
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

    if not settings.sheets_configured:
        logger.warning("Google Sheets not configured — skipping sheet log.")
        return False

    try:
        credentials = _get_credentials()
        service = build("sheets", "v4", credentials=credentials, cache_discovery=False)

        submitted_at = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")
        row = [
            submitted_at,
            enquiry.name,
            enquiry.company_name or "",
            enquiry.phone,
            enquiry.email or "",
            enquiry.location,
            enquiry.service,
            enquiry.workers_or_vehicles or "",
            enquiry.message,
            enquiry.language,
        ]

        service.spreadsheets().values().append(
            spreadsheetId=settings.google_sheet_id,
            range=f"{settings.google_sheet_tab}!A1",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={"values": [row]},
        ).execute()
        return True
    except HttpError:
        logger.exception("Google Sheets API rejected the append (check sharing / sheet id / tab name)")
        return False
    except Exception:
        logger.exception("Failed to append enquiry to Google Sheets")
        return False
