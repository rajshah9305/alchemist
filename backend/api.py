# backend/api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .models import Interaction
from .database import get_db
from ai_engine import load_codestral_model, MemorySystem, PersonalityManager

router = APIRouter()
model = load_codestral_model()
memory_system = MemorySystem()
personality_manager = PersonalityManager()

class InteractionRequest(BaseModel):
    prompt: str

@router.post("/interact")
async def interact(request: InteractionRequest):
    personality = personality_manager.get_current_personality()
    response = model.generate_response(request.prompt, personality)
    interaction = Interaction(prompt=request.prompt, response=response)
    memory_system.add_interaction(interaction.dict())
    return interaction

@router.get("/memory")
async def get_memory():
    return memory_system.get_memory()

@router.delete("/memory")
async def clear_memory():
    memory_system.clear_memory()
    return {"message": "Memory cleared"}