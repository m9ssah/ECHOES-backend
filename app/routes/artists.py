from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

artists_router = APIRouter()

@artists_router.get("/artist/{artist_id}")
def get_artist(artist_id: str):
    return ArtistService.fetch_artist(artist_id)
