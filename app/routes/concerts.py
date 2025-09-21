from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

concerts_router = APIRouter()

@concerts_router.get("/concerts")
def get_concerts(artist_name: str):
    return ConcertService.search_concerts(artist_name)
