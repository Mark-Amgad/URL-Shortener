from fastapi import FastAPI
from app.routers.url import router as url_router
from app.database import engine,Base
from . import models

#models.Base.metadata.create_all(bind = engine)
Base.metadata.create_all(bind = engine)


app = FastAPI()


app.include_router(url_router)


@app.get("/")
async def root():
    return {"message" : "Hello, Mark is here"}