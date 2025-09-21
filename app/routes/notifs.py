from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/notifs/action")
def notifs_action(request: Request):
    return JSONResponse({"message": f"Notifs action successful"})
