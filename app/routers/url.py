from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.url import URLCreate, URLRead
from app.crud.url import create_url,get_all_urls

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    # dependencies=[Depends(get_token_header)], # TODO: in phase 2 after adding auth
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=URLRead)
def create_shortened_url(url_data: URLCreate, db: Session = Depends(get_db)):
    return create_url(db=db, url_data=url_data)

@router.get("/", response_model=List[URLRead])
def get_shortened_urls(db: Session = Depends(get_db)):
    urls = get_all_urls(db=db, limit=10,skip=0)
    return urls