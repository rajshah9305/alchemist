# backend/main.py
from fastapi import FastAPI
from .api import router
from .database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(router)