from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    shortened_url = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    expires_at = Column(TIMESTAMP, nullable=True)
    clicks = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)