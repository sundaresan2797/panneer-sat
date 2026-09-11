import re

from pydantic import BaseModel, EmailStr, Field, field_validator

PHONE_RE = re.compile(r"^[0-9+\-\s()]{7,20}$")


class EnquiryIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    company_name: str | None = Field(default=None, max_length=150)
    phone: str = Field(..., min_length=7, max_length=20)
    email: EmailStr | None = None
    location: str = Field(..., min_length=2, max_length=150)
    service: str = Field(..., min_length=2, max_length=100)
    workers_or_vehicles: str | None = Field(default=None, max_length=50)
    message: str = Field(..., min_length=5, max_length=2000)
    language: str = Field(default="en", max_length=2)

    # Honeypot field — real users never fill this in; bots usually do.
    website: str | None = Field(default=None, max_length=200)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not PHONE_RE.match(v):
            raise ValueError("Enter a valid phone number.")
        return v

    @field_validator("language")
    @classmethod
    def validate_language(cls, v: str) -> str:
        if v not in ("en", "ta"):
            return "en"
        return v

    @field_validator("name", "location", "service", "message", "company_name", "workers_or_vehicles")
    @classmethod
    def strip_text(cls, v: str | None) -> str | None:
        if v is None:
            return v
        return v.strip()


class EnquiryOut(BaseModel):
    success: bool
    message: str
