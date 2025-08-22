from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from app.services.auth_service import AuthService

router = APIRouter()

@router.get("/spotify/login")
def spotify_login():
    url = AuthService.spotify_login()
    return RedirectResponse(url)

@router.get("/spotify/callback")
def spotify_callback(request: Request):
    return {"message": "Spotify login successful"}
