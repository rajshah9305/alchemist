# backend/api.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import logging
import os
import sys

from .models import Interaction
from .database import insert_interaction, get_all_interactions, clear_interactions

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add the project root to the path to import ai_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    # Import AI engine components 
    from ai_engine import load_codestral_model, MemorySystem, PersonalityManager
    logger.info("Successfully imported AI engine components")
    
    # Initialize AI components
    model = load_codestral_model()
    memory_system = MemorySystem()
    personality_manager = PersonalityManager()
    
    USING_REAL_AI = True
    logger.info("Using real AI components")
    
except ImportError as e:
    logger.warning(f"Could not import AI engine components: {e}")
    logger.warning("Using mock AI components instead")
    
    # Use mock components if imports fail
    from .mock_ai_engine import load_codestral_model, MemorySystem, PersonalityManager
    
    model = load_codestral_model()
    memory_system = MemorySystem()
    personality_manager = PersonalityManager()
    
    USING_REAL_AI = False

# Initialize router
router = APIRouter()

# Request models
class InteractionRequest(BaseModel):
    prompt: str

class InteractionResponse(BaseModel):
    prompt: str
    response: str
    timestamp: str

# Dependency to get AI components
def get_ai_components():
    return {
        "model": model,
        "memory_system": memory_system,
        "personality_manager": personality_manager
    }

@router.post("/interact", response_model=InteractionResponse)
async def interact(
    request: InteractionRequest, 
    components: Dict[str, Any] = Depends(get_ai_components)
):
    """Process an interaction with the AI model."""
    try:
        # Get model components
        model = components["model"]
        memory_system = components["memory_system"]
        personality_manager = components["personality_manager"]
        
        # Log the request
        logger.info(f"Received interaction request: {request.prompt[:50]}...")
        
        # Generate response
        personality = personality_manager.get_current_personality()
        response = model.generate_response(request.prompt, personality)
        
        # Create interaction
        interaction = Interaction(prompt=request.prompt, response=response)
        
        # Store in memory system
        memory_system.add_interaction(interaction.dict())
        
        # Store in database
        insert_interaction(interaction)
        
        logger.info(f"Processed interaction successfully")
        return interaction
    except Exception as e:
        logger.error(f"Error processing interaction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing interaction: {str(e)}")

@router.get("/memory", response_model=List[Dict[str, Any]])
async def get_memory(components: Dict[str, Any] = Depends(get_ai_components)):
    """Get the in-memory history of interactions."""
    try:
        memory_system = components["memory_system"]
        memory = memory_system.get_memory()
        logger.info(f"Retrieved memory with {len(memory)} entries")
        return memory
    except Exception as e:
        logger.error(f"Error retrieving memory: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving memory: {str(e)}")

@router.get("/history", response_model=List[Dict[str, Any]])
async def get_history():
    """Get the database history of interactions."""
    try:
        history = get_all_interactions()
        logger.info(f"Retrieved history with {len(history)} entries")
        return history
    except Exception as e:
        logger.error(f"Error retrieving history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error retrieving history: {str(e)}")

@router.delete("/memory")
async def clear_memory(components: Dict[str, Any] = Depends(get_ai_components)):
    """Clear the in-memory history."""
    try:
        memory_system = components["memory_system"]
        memory_system.clear_memory()
        logger.info("Memory cleared")
        return {"message": "Memory cleared"}
    except Exception as e:
        logger.error(f"Error clearing memory: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error clearing memory: {str(e)}")

@router.delete("/history")
async def clear_history():
    """Clear the database history."""
    try:
        deleted = clear_interactions()
        logger.info(f"History cleared, {deleted} records deleted")
        return {"message": f"History cleared, {deleted} records deleted"}
    except Exception as e:
        logger.error(f"Error clearing history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error clearing history: {str(e)}")

@router.get("/status")
async def get_status():
    """Get the status of the AI system."""
    return {
        "status": "operational",
        "using_real_ai": USING_REAL_AI,
        "memory_size": len(memory_system.get_memory()),
        "personality": personality_manager.get_current_personality()["system_message"]
    }
