"""Optional notification after durable storage; never shares SAT's inbox."""

import logging
import smtplib
from email.message import EmailMessage

from app.config import get_settings
from app.content.sagbs import SERVICE_MAP

logger = logging.getLogger("sagbs.email")


def notify_enquiry(enquiry, reference):
    settings = get_settings()
    if not (settings.smtp_host and settings.smtp_username and settings.smtp_password and settings.sagbs_email):
        return "unconfigured"
    try:
        message = EmailMessage()
        message["Subject"] = f"SAGBS — New {enquiry.kind} enquiry — {reference[:8]}"
        message["From"] = settings.smtp_username
        message["To"] = settings.sagbs_email
        message["Reply-To"] = str(enquiry.email)
        service = SERVICE_MAP.get(enquiry.service, {}).get("title", "Help choosing a service")
        message.set_content("\n".join([
            f"Reference: {reference}", f"Name: {enquiry.name}", f"Company: {enquiry.company_name or '-'}",
            f"Email: {enquiry.email}", f"Phone: {enquiry.phone}", f"Country: {enquiry.country}",
            f"Service: {service}", f"Engagement: {enquiry.engagement}",
            f"Budget band (INR): {enquiry.budget or 'Not specified'}", "", enquiry.message,
        ]))
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=8) as server:
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(message)
        return "sent"
    except Exception as exc:
        logger.error("SAGBS notification failed (%s); enquiry remains stored.", type(exc).__name__)
        return "failed"
