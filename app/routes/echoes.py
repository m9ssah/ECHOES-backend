from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/echoes/action")
def echoes_action(request: Request):
    return JSONResponse({"message": "Echoes action successful"})
