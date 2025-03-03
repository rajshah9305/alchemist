from fastapi import APIRouter, Request

from backend.utils import session

router = APIRouter()

@router.get("/history")
async def history(request: Request):
    chat_history = session.get_chat_history(request)
    return {"chat_history": chat_history}