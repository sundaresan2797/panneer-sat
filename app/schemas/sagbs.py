import re
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.content.sagbs import SERVICE_MAP


class SAGBSEnquiryIn(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: str = Field(min_length=2, max_length=100)
    company_name: str = Field(default="", max_length=150)
    email: EmailStr = Field(max_length=254)
    phone: str = Field(min_length=7, max_length=25)
    country: str = Field(min_length=2, max_length=100)
    service: str = Field(min_length=2, max_length=100)
    engagement: Literal["project", "monthly", "dedicated", "maintenance", "discuss"] = "discuss"
    budget: Literal["", "under-25k", "25k-75k", "75k-2l", "2l-plus", "discuss"] = ""
    message: str = Field(min_length=20, max_length=5000)
    consent: Literal[True]
    kind: Literal["contact", "quote"] = "contact"
    submission_id: UUID = Field(default_factory=uuid4)
    website: str = Field(default="", max_length=200)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not re.fullmatch(r"[+\d\s().-]+", value) or not 7 <= len(re.sub(r"\D", "", value)) <= 15:
            raise ValueError("Enter 7–15 numbers, with your country code. For example: +91 9876543210.")
        return value

    @field_validator("service")
    @classmethod
    def validate_service(cls, value):
        if value not in SERVICE_MAP and value != "discuss":
            raise ValueError("Choose a service from the list.")
        return value


class SAGBSEnquiryOut(BaseModel):
    success: bool
    message: str
    reference: str | None = None
