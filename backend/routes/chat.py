from fastapi import APIRouter, Request
from pydantic import BaseModel

from backend.utils import session

router = APIRouter()

class ChatMessage(BaseModel):
    role: str
    content: str

@router.post("/chat")
async def chat(request: Request, chat_message: ChatMessage):
    chat_history = session.get_chat_history(request)
    chat_history.append(chat_message.dict())
    session.set_chat_history(request, chat_history)
    return {"response": "Your response here"}