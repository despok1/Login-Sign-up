from database import Database
from typing import Union
from fastapi import FastAPI
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


@app.post("/register")
def register(request: RegisterRequest):
    database = Database(user_email=request.user_email, password=request.password,full_name=request.full_name)
    result = database.registration()
    return { "user_exist": result}

@app.post("/login")
def login(request: LoginRequest):
    database = Database(user_email=request.user_email, password=request.password, full_name="")
    result = database.check_user_for_login(user_email=request.user_email, password=request.password)
    return result


