import logging
import smtplib
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import ZoneInfo

from app.config import get_settings
from app.schemas.enquiry import EnquiryIn

logger = logging.getLogger("sat.email")


def _build_message(enquiry: EnquiryIn) -> str:
    submitted_at = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y, %I:%M %p IST")
    lines = [
        f"Name: {enquiry.name}",
        f"Company: {enquiry.company_name or '-'}",
        f"Phone: {enquiry.phone}",
        f"Email: {enquiry.email or '-'}",
        f"Location: {enquiry.location}",
        f"Service: {enquiry.service}",
        f"Workers / Vehicles: {enquiry.workers_or_vehicles or '-'}",
        f"Language: {enquiry.language}",
        "",
        "Requirement:",
        enquiry.message,
        "",
        f"Submitted: {submitted_at}",
    ]
    return "\n".join(lines)


def send_enquiry_email(enquiry: EnquiryIn) -> bool:
    """Send the enquiry to the company inbox. Returns False (never raises)
    if SMTP isn't configured or sending fails, so the API can still confirm
    the enquiry was received and log it for manual follow-up."""
    settings = get_settings()

    if not settings.email_configured:
        logger.warning("SMTP not configured — enquiry logged only.\n%s", _build_message(enquiry))
        return False

    msg = EmailMessage()
    msg["Subject"] = "New Website Enquiry — Sri Annamalayar Transport & Logistics"
    msg["From"] = settings.smtp_username
    msg["To"] = settings.contact_email
    if enquiry.email:
        msg["Reply-To"] = enquiry.email
    msg.set_content(_build_message(enquiry))

    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=10) as server:
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(msg)
        return True
    except Exception:
        logger.exception("Failed to send enquiry email")
        return False
