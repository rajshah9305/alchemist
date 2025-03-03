from fastapi import APIRouter, Request

from backend.utils import session

router = APIRouter()

@router.get("/mode")
async def mode(request: Request):
    mode = session.get_mode(request)
    return {"mode": mode}

@router.post("/mode")
async def switch_mode(request: Request):
    mode = session.switch_mode(request)
    return {"mode": mode}