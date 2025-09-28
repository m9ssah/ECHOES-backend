from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.services.auth_service import AuthService
from pydantic import BaseModel

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin):
    # Implement login logic here
    return {"message": "Login successful"}

@router.get("/spotify/callback")
def spotify_callback(request: Request):
    return {"message": "Spotify login successful"}
