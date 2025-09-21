from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/songs/action")
def songs_action(request: Request):
    return JSONResponse({"message": f"Songs action successful"})
