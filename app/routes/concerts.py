from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/concerts/action")
def concerts_action(request: Request):
    return JSONResponse({"message": "Concerts action successful"})
