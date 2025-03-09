# backend/models.py
from pydantic import BaseModel
from typing import Optional
import datetime

class Interaction(BaseModel):
    prompt: str
    response: str
    timestamp: Optional[str] = None
    
    def __init__(self, **data):
        if 'timestamp' not in data:
            data['timestamp'] = datetime.datetime.now().isoformat()
        super().__init__(**data)
