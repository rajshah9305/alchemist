from pydantic import BaseModel, validator
from typing import Optional
import datetime

class Interaction(BaseModel):
    prompt: str
    response: str
    timestamp: Optional[datetime.datetime] = None
    
    @validator('timestamp', pre=True, always=True)
    def set_timestamp(cls, value):
        return value or datetime.datetime.now()

# Example usage
interaction = Interaction(prompt="Hello", response="Hi there!")
print(interaction)
