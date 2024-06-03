from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import engine, Base
from .routers import users, entities

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(entities.router, prefix="/entities", tags=["entities"])

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
