from pydantic import BaseModel, field_validator
from typing import Optional
import re

class EnquiryModel(BaseModel):
    name: str
    email: str
    phone: str
    option: str
    school_name: Optional[str] = None
    city_state: Optional[str] = None
    requirement: Optional[str] = None
    query: Optional[str] = None

    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v

    @field_validator('email')
    def validate_email(cls, v):
        # Basic email regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, v):
            raise ValueError('Invalid email format')
        return v

    @field_validator('phone')
    def validate_phone(cls, v):
        # Allow digits, spaces, dashes, plus sign. Min 10 digits.
        digits = re.sub(r'\D', '', v)
        if len(digits) < 10:
            raise ValueError('Phone number must have at least 10 digits')
        return v

    @field_validator('option')
    def validate_option(cls, v):
        allowed_options = ['atl', 'stem', 'refill', 'school', 'other']
        if v not in allowed_options:
            raise ValueError(f'Option must be one of {allowed_options}')
        return v
