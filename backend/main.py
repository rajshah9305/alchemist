# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from .api import router
from .database import init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO if os.getenv("LOGLEVEL", "INFO") != "DEBUG" else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Alchemist API", 
    description="Backend API for the Alchemist conversation system",
    version="0.1.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize components on application startup."""
    try:
        # Initialize database
        init_db()
        logger.info("Database initialized successfully")
        
        # Check if the Codestral model exists
        ai_engine_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ai_engine')
        model_path = os.path.join(ai_engine_path, 'codestral_25.01.model')
        
        if os.path.exists(model_path):
            logger.info(f"Codestral model found at: {model_path}")
        else:
            logger.warning(f"Codestral model not found at: {model_path}. Will use fallback.")
            
        # Check if personality config exists
        config_path = os.path.join(ai_engine_path, 'personality_config.yaml')
        if os.path.exists(config_path):
            logger.info(f"Personality config found at: {config_path}")
        else:
            logger.warning(f"Personality config not found at: {config_path}. Will use defaults.")
            
    except Exception as e:
        logger.error(f"Error during startup: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during startup")

# Include routers
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    """Root endpoint for the API."""
    return {
        "message": "Welcome to the Alchemist API", 
        "documentation": "/docs",
        "api_endpoints": "/api"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Example health check logic (extend as needed)
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Health check failed")
