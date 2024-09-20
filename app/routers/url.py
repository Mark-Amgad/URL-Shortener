from fastapi import APIRouter, Depends,HTTPException
from typing_extensions import Annotated
from typing import List
from sqlalchemy.orm import Session
from app.dependencies import get_db,Pagination
from app.schemas.url import URLCreate, URLRead, URLUpdate
import validators
from app.crud.url import create_one,get_all,update_one,get_one,delete_one

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    # dependencies=[Depends(get_token_header)], # TODO: in phase 2 after adding auth
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=URLRead)
def create_shortened_url(url_data: URLCreate, db: Session = Depends(get_db)):
    if not validators.url(url_data.original_url):
        raise HTTPException(status_code=400, detail="Your provided URL is not valid")
    
    return create_one(db=db, url_data=url_data)

@router.get("/", response_model=List[URLRead])
def get_shortened_urls(pagination:Annotated[Pagination, Depends(Pagination)],db: Session = Depends(get_db)):
    urls = get_all(db=db, limit=pagination.limit,skip=pagination.skip)
    return urls

@router.patch("/{id}" , response_model=URLRead)
def update_shortened_url(id:int,url_data_body:URLUpdate, db:Session = Depends(get_db)):
    return update_one(db,id,url_data_body)

@router.get("/{shortened_url}",response_model=URLRead)
def get_one_url(shortened_url:str,db:Session = Depends(get_db)):
    return get_one(db,shortened_url)

@router.delete("/{id}")
def delete_url_by_id(id:int,db:Session = Depends(get_db)):
    return delete_one(db,id)

