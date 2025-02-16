from database import Database
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# run server: uvicorn main:app
# run server:  fastapi dev main.py

class RegisterRequest(BaseModel):
    user_email: str
    password: str
    full_name: str

class LoginRequest(BaseModel):
    user_email: str
    password: str

    
    
    
app = FastAPI()

# Добавляем поддержку CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т. д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
def main_page():
    return "Server home page"

# Login
@app.post("/login")
def login(request: LoginRequest):
    database = Database(user_email=request.user_email, password=request.password, full_name="")
    result = database.check_user_for_login(user_email=request.user_email, password=request.password)
    return { "isLoginSuccess": result }


# Regestration
@app.post("/register")
def register(request: RegisterRequest):
    database = Database(user_email=request.user_email, password=request.password,full_name=request.full_name)
    result = database.registration()
    return { "userExist": result}


