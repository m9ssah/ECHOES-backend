from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import Keys
from app.routes import auth, notifs, recomendations, reviews, songs, users, concerts, artists, feed, echoes
app = FastAPI(title="ECHOES", version="1.0.0")

origins = ["http://localhost:3000"]    # TODO: add frontend domain l8r

app.add_middleware(CORSMiddleware, 
                   allow_origins=origins, 
                   allow_methods=["POST", "GET", "OPTIONS", "DELETE"], 
                   allow_credentiasl=True,
                   allow_headers=["*"]
                   )

@app.route("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Backend is running."}

# API Routers connections
app.include_router(auth.router, prefix="app/routes/auth", tags=["Auth"])
app.include_router(users.router, prefix="app/routes/users", tags=["Users"])
app.include_router(songs.router, prefix="app/route/songs", tags=["Songs"])
app.include_router(artists.router, prefix="app/route/artists", tags=["Artists"])
app.include_router(reviews.router, prefix="app/route/reviews", tags=["Reviews"])
app.include_router(recomendations.router, prefix="app/route/recomemendations", tags=["Recommendations"])
app.include_router(concerts.router, prefix="app/route/concerts", tags=["Concert"])
app.include_router(notifs.router, prefix="app/route/notifs", tags=["Notifications"])
app.include_router(echoes.router, prefix="app/route/echoes", tags=["Echoes"])
app.include_router(feed.router, prefix="app/route/ffed", tags=["Feed"])

if __name__ == "__main__":
    PORT=(Keys.PORT)
    app.run