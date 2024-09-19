from app.database import SessionLocal
from fastapi import Query


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Pagination:
    def __init__(self,skip:int = 0, limit:int = 10):
        self.skip = skip
        self.limit = limit
