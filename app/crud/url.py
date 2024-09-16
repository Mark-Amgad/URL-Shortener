from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from typing import List, Optional

from app.models.url import Url
from app.schemas.url import URLCreate, URLUpdate

def create_url(db:Session, url_data:URLCreate) -> Url:
    if url_data.shortened_url is None:
        raise HTTPException(status_code=400, detail="Shortened URL not fount and not supported to generate it by the server till now.")

    existUrl = db.query(Url).filter(Url.shortened_url == url_data.shortened_url).first()

    if existUrl is not None:
        raise HTTPException(status_code=400, detail="Shortened URL already exists")
    
    db_url = Url(
        original_url = url_data.original_url,
        shortened_url = url_data.shortened_url,
        created_at = datetime.utcnow()
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_all_urls(db:Session, skip: int = 0, limit:int = 10) -> List[Url]:
    return db.query(Url).offset(skip).limit(limit).all()


def update_url(db:Session, id:int, url_data:URLUpdate)-> Url:
    url_db = db.query(Url).filter(Url.id == id).first()
    if url_db is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    if url_data.original_url is not None:
        url_db.original_url = url_data.original_url
    
    if url_data.is_active is not None:
        url_db.is_active = url_data.is_active
    
    db.commit()
    db.refresh(url_db)

    return url_db
    
def get_one_url_by_shortened_url(db:Session, shortened_url)-> Url:
    url = db.query(Url).filter(Url.shortened_url == shortened_url).first()
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return url

