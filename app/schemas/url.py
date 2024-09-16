from typing import Optional
from pydantic import BaseModel, AnyHttpUrl # TODO: add validation using AnyHttpUrl
from datetime import datetime

# Base schema for common properties
class URLBase(BaseModel):
    original_url: str
    is_active: Optional[bool] = True

# For Post method
class URLCreate(URLBase):
    shortened_url: str

# PATCH or PUT
class URLUpdate(BaseModel):
    original_url: Optional[str] = None
    expires_at: Optional[datetime] = None
    is_active: Optional[bool] = None

# Schema for reading URL data (response schema)
class URLRead(URLBase):
    id: int
    shortened_url: str

    created_at: datetime
    expires_at: Optional[datetime] = None
    clicks: int

    class Config:
        orm_mode = True  # This allows returning SQLAlchemy models as responses

# DELETE method
class URLDelete(BaseModel):
    is_active: Optional[bool] = False