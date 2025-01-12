from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests

app = FastAPI()

# Ваш CLIENT_ID из Google Cloud Console
CLIENT_ID = "YOUR_CLIENT_ID"

# Модель данных для получения токена от клиента
class CredentialRequest(BaseModel):
    credential: str

@app.post("/google_login")
async def google_login(data: CredentialRequest):
    try:
        # Проверяем токен, отправленный клиентом
        token = data.credential
        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        
        # id_info содержит данные пользователя, например:
        user_id = id_info["sub"]
        email = id_info["email"]
        name = id_info["name"]
        picture = id_info.get("picture")

        # Вернуть информацию о пользователе
        return {
            "message": "Login successful!",
            "user": {
                "id": user_id,
                "email": email,
                "name": name,
                "picture": picture,
            }
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid token")

# Главная страница (опционально)
@app.get("/")
async def home():
    return {"message": "Google Sign-In API is running!"}