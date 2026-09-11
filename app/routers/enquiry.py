import logging

from fastapi import APIRouter

from app.schemas.enquiry import EnquiryIn, EnquiryOut
from app.services.email_service import send_enquiry_email
from app.services.sheets_service import append_enquiry_to_sheet

logger = logging.getLogger("sat.enquiry")
router = APIRouter()

SUCCESS_MESSAGE = {
    "en": "Your enquiry has been submitted successfully.",
    "ta": "உங்கள் கோரிக்கை வெற்றிகரமாக அனுப்பப்பட்டது.",
}


@router.post("/api/enquiry", response_model=EnquiryOut)
def submit_enquiry(enquiry: EnquiryIn):
    # Honeypot: silently "succeed" without emailing/logging as a real lead.
    if enquiry.website:
        return EnquiryOut(success=True, message=SUCCESS_MESSAGE.get(enquiry.language, SUCCESS_MESSAGE["en"]))

    send_enquiry_email(enquiry)
    append_enquiry_to_sheet(enquiry)
    logger.info("Enquiry received from %s (%s) — %s", enquiry.name, enquiry.phone, enquiry.service)

    return EnquiryOut(success=True, message=SUCCESS_MESSAGE.get(enquiry.language, SUCCESS_MESSAGE["en"]))
