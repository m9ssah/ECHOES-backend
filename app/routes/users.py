from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/users/action")
def users_action(request: Request):
    return JSONResponse({"message": f"Users action successful"})
