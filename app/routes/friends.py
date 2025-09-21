from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/friends/action")
def friends_action(request: Request):
    return JSONResponse({"message": "Friends action successful"})
