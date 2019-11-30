from pydantic import BaseModel


class RegisterUserRequest(BaseModel):
    user_name: str
    password: str


class RegisterUserResponse(BaseModel):
    success: bool
    message: str


class LoginRequest(BaseModel):
    user_name: str
    password: str


class LoginResponse(BaseModel):
    success: bool


class SubmissionResponse(BaseModel):
    success: bool
    message: str
    score: float = 0
