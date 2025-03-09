# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router
from .database import init_db

app = FastAPI(title="Alchemist API", 
              description="Backend API for the Alchemist conversation system",
              version="0.1.0")

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    try:
        init_db()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error during startup: {e}")

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Alchemist API. Use /api endpoints to interact with the system."}
