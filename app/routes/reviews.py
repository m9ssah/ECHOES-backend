from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/<feature>/action")
def reviews_action(request: Request):
    return JSONResponse({"message": f"Reviews action successful"})
