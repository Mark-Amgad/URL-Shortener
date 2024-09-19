from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from typing import List, Optional

from app.models.url import Url
from app.schemas.url import URLCreate, URLUpdate
from app.utils.url import generate_short_url

def create_one(db:Session, url_data:URLCreate) -> Url:
    

    generated_shortened_url = generate_short_url()
    while db.query(Url).filter(Url.shortened_url == generated_shortened_url).first() is not None:
        generated_shortened_url = generate_short_url()

    
    
    db_url = Url(
        original_url = url_data.original_url,
        shortened_url = generated_shortened_url,
        created_at = datetime.utcnow()
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_all(db:Session, skip: int = 0, limit:int = 10) -> List[Url]:
    return db.query(Url).offset(skip).limit(limit).all()


def update_one(db:Session, id:int, url_data:URLUpdate)-> Url:
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
    
def get_one(db:Session, shortened_url)-> Url:
    url = db.query(Url).filter(Url.shortened_url == shortened_url).first()
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return url

def delete_one(db:Session, id:int)-> str:
    url = db.query(Url).filter(Url.id == id).first()
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")

    db.delete(url)
    db.commit()

    return {"message": "Deleted Successfully"}