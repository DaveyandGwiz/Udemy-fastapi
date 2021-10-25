from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine   #new
from databases import Database
from db.base import Base  #new



def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    return app

def create_tables():
    Base.metadata.create_all(bind=engine)


app = start_application()

@app.get("/")
def hello_api_BUT_BETTER():
    return {"messy": "hello world!"}

