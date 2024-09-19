from fastapi import FastAPI
from app.routers.url import router as url_router
from app.database import engine,Base
from . import models

Base.metadata.create_all(bind = engine)


app = FastAPI()


app.include_router(url_router)


@app.get("/",tags=['health'])
async def health():
    return {"message" : "Hello, Mark is here"}