from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(f"/recommendations/action")
def recommendations_action(request: Request):
    return JSONResponse({"message": f"Recommendations action successful"})
