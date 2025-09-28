from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes import (
    auth,
    notifs,
    recommendations,
    reviews,
    songs,
    users,
    concerts,
    artists,
    feed,
    echoes,
)

app = FastAPI(title="ECHOES", version="1.0.0")

origins = ["http://localhost:3000"]  # TODO: add frontend domain l8r

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["POST", "GET", "OPTIONS", "DELETE"],
    allow_credentials=True,
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Backend is running."}


# API Routers connections
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(songs.router, prefix="/songs", tags=["Songs"])
app.include_router(artists.router, prefix="/artists", tags=["Artists"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(
    recommendations.router, prefix="/recommendations", tags=["Recommendations"]
)
app.include_router(concerts.router, prefix="/concerts", tags=["Concert"])
app.include_router(notifs.router, prefix="/notifs", tags=["Notifications"])
app.include_router(echoes.router, prefix="/echoes", tags=["Echoes"])
app.include_router(feed.router, prefix="/feed", tags=["Feed"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
