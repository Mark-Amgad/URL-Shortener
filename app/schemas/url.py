from typing import Optional
from pydantic import BaseModel, AnyHttpUrl # TODO: add validation using AnyHttpUrl
from datetime import datetime

class URLBase(BaseModel):
    original_url: str
    is_active: Optional[bool] = True

class URLCreate(URLBase):
    pass

class URLUpdate(BaseModel):
    original_url: Optional[str] = None
    expires_at: Optional[datetime] = None
    is_active: Optional[bool] = None

class URLRead(URLBase):
    id: int
    shortened_url: str

    created_at: datetime
    expires_at: Optional[datetime] = None
    clicks: int

    class Config:
        orm_mode = True

class URLDelete(BaseModel):
    is_active: Optional[bool] = False