# backend/models.py
from pydantic import BaseModel
from typing import Optional

class Interaction(BaseModel):
    prompt: str
    response: str
    timestamp: Optional[str] = None