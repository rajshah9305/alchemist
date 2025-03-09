# backend/api.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from .models import Interaction
from .database import insert_interaction, get_all_interactions, clear_interactions

# Mock implementations for the AI engine components
# These should be replaced with actual implementations
class MockAIModel:
    def generate_response(self, prompt: str, personality: Dict[str, Any]) -> str:
        return f"Response to: {prompt}"

class MockMemorySystem:
    def __init__(self):
        self.memory = []
        
    def add_interaction(self, interaction: Dict[str, Any]):
        self.memory.append(interaction)
        
    def get_memory(self) -> List[Dict[str, Any]]:
        return self.memory
        
    def clear_memory(self):
        self.memory = []

class MockPersonalityManager:
    def get_current_personality(self) -> Dict[str, Any]:
        return {"style": "helpful", "tone": "friendly"}

# Initialize router and components
router = APIRouter()

# Create dependency for AI components
def get_ai_components():
    model = MockAIModel()
    memory_system = MockMemorySystem()
    personality_manager = MockPersonalityManager()
    return {"model": model, "memory_system": memory_system, "personality_manager": personality_manager}

# Request models
class InteractionRequest(BaseModel):
    prompt: str

class InteractionResponse(BaseModel):
    prompt: str
    response: str
    timestamp: str

@router.post("/interact", response_model=InteractionResponse)
async def interact(
    request: InteractionRequest, 
    components: Dict[str, Any] = Depends(get_ai_components)
):
    try:
        # Get model components
        model = components["model"]
        memory_system = components["memory_system"]
        personality_manager = components["personality_manager"]
        
        # Generate response
        personality = personality_manager.get_current_personality()
        response = model.generate_response(request.prompt, personality)
        
        # Create interaction
        interaction = Interaction(prompt=request.prompt, response=response)
        
        # Store in memory system
        memory_system.add_interaction(interaction.dict())
        
        # Store in database
        insert_interaction(interaction)
        
        return interaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing interaction: {str(e)}")

@router.get("/memory", response_model=List[Dict[str, Any]])
async def get_memory(components: Dict[str, Any] = Depends(get_ai_components)):
    try:
        memory_system = components["memory_system"]
        return memory_system.get_memory()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving memory: {str(e)}")

@router.get("/history", response_model=List[Dict[str, Any]])
async def get_history():
    try:
        return get_all_interactions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving history: {str(e)}")

@router.delete("/memory")
async def clear_memory(components: Dict[str, Any] = Depends(get_ai_components)):
    try:
        memory_system = components["memory_system"]
        memory_system.clear_memory()
        return {"message": "Memory cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing memory: {str(e)}")

@router.delete("/history")
async def clear_history():
    try:
        deleted = clear_interactions()
        return {"message": f"History cleared, {deleted} records deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing history: {str(e)}")
