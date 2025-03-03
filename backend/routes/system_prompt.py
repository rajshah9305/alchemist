from fastapi import APIRouter, Request

from backend.utils import session

router = APIRouter()

@router.get("/system_prompt")
async def system_prompt(request: Request):
    system_prompt = session.get_system_prompt(request)
    return {"system_prompt": system_prompt}

@router.post("/system_prompt")
async def set_system_prompt(request: Request, system_prompt: str):
    session.set_system_prompt(request, system_prompt)
    return {"system_prompt": system_prompt}