
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/feed/action")
def feed_action(request: Request):
    return JSONResponse({"message": "Feed action successful"})
