from supabase import create_client
from app.config import settings

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

class SupabaseService: 
    @staticmethod 
    def insert_song(user_id: str, track: dict): 
        data, error = supabase.table("songs").insert({
            "user_id": user_id,
            "title": track["name"],
            "artist": track["artists"][0]["name"],
            "spotify_id": track["id"]
        }).execute()
        return data, error
    
