import logging
from collections import OrderedDict
from threading import Lock
from time import monotonic

from fastapi import APIRouter, HTTPException, Request

from app.schemas.sagbs import SAGBSEnquiryIn, SAGBSEnquiryOut
from app.services.sheets_service import append_sagbs_contact_to_sheet
from app.services.sagbs_email import notify_enquiry
from app.services.sagbs_store import SubmissionConflict, save_enquiry, set_notification_status

logger = logging.getLogger("sagbs.enquiries")
router = APIRouter(prefix="/sagbs/api", tags=["SAGBS enquiries"])

# A bounded, per-process burst guard. Configure an edge limit for multi-worker production.
_requests = OrderedDict()
_lock = Lock()


def check_rate_limit(address):
    now = monotonic()
    with _lock:
        recent = [t for t in _requests.pop(address, []) if now - t < 600]
        if len(recent) >= 8:
            _requests[address] = recent
            raise HTTPException(429, "You have sent several messages. Please wait 10 minutes before trying again, or email us.", headers={"Retry-After": "600"})
        _requests[address] = recent + [now]
        while len(_requests) > 5000:
            _requests.popitem(last=False)


@router.post("/enquiries", response_model=SAGBSEnquiryOut, status_code=201,
             responses={409: {"description": "Submission reference already used"},
                        422: {"description": "Invalid enquiry"}, 429: {"description": "Rate limited"},
                        503: {"description": "Enquiry was not stored; retry or email"}})
def submit_enquiry(enquiry: SAGBSEnquiryIn, request: Request):
    check_rate_limit(request.client.host if request.client else "unknown")
    if enquiry.website:
        return SAGBSEnquiryOut(success=True, message="Thank you for your message.")
    try:
        reference, created = save_enquiry(enquiry)
    except SubmissionConflict as exc:
        raise HTTPException(409, str(exc)) from exc
    except Exception as exc:
        logger.error("SAGBS enquiry storage unavailable (%s).", type(exc).__name__)
        raise HTTPException(503, "We could not save your message. Please try again or email us.") from exc

    if created:
        if enquiry.kind == "contact":
            append_sagbs_contact_to_sheet(enquiry, reference)
        status = notify_enquiry(enquiry, reference)
        try:
            set_notification_status(reference, status)
        except Exception as exc:
            logger.error("Could not update notification status (%s).", type(exc).__name__)
    return SAGBSEnquiryOut(success=True, reference=reference,
                          message="Thank you. Your message has been saved for our team to read.")
