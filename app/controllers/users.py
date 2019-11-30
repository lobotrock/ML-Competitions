from fastapi import APIRouter

from di import user_service
from models import RegisterUserResponse, RegisterUserRequest, LoginRequest, LoginResponse

app = APIRouter()


@app.post("/register/", response_model=RegisterUserResponse)
async def register_user(new_user: RegisterUserRequest):
    return await user_service.create_new_user(new_user.user_name, new_user.password)


@app.post("/login/", response_model=LoginResponse)
async def login_user(login_request: LoginRequest):
    return await user_service.check_login(login_request.user_name, login_request.password)


@app.post("/update/")
async def update_user():
    return "TODO"