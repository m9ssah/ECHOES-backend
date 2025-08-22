from app.utils.supabase_client import supabase
from fastapi import HTTPException

class AuthService:
    
    @staticmethod
    def signup_email(email: str, password: str):
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return response

    @staticmethod
    def login_email(email: str, password: str):
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if "error" in response:
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return response

    @staticmethod
    def spotify_login():
        response = supabase.auth.sign_in_with_oauth({
            "provider": "spotify",
            "options": {"redirect_to": "http://localhost:8000/auth/spotify/callback"}
        })
        return response.url

    @staticmethod
    def get_user(session_token: str):
        response = supabase.auth.get_user(session_token)
        if "error" in response:
            raise HTTPException(status_code=401, detail="Expired/invalid token")
        return response.user
    
