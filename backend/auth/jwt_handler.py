# File: /backend/auth/jwt_handler.py
# Description: Functions for handling JWT authentication, including generating and verifying tokens.
# Author: [Your Name]
# Created: [Date]

import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings, Field, validator

from backend.models.user import User


class Settings(BaseSettings):
    """Configuration for JWT handling sourced from environment variables."""

    secret_key: str = Field(..., env="SECRET_KEY", description="Secret key for signing JWTs")
    algorithm: str = Field("HS256", env="ALGORITHM", description="JWT signing algorithm")
    access_token_expire_minutes: int = Field(
        30,
        env="ACCESS_TOKEN_EXPIRE_MINUTES",
        description="Access token expiry duration in minutes",
    )

    @validator("secret_key")
    def validate_secret_key(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("SECRET_KEY must not be empty")
        return value

    @validator("access_token_expire_minutes")
    def validate_expiry(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES must be a positive integer")
        return value

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Temporary in-memory user store for demonstration purposes
_fake_users_db = {
    "johndoe": {
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "hashed_password": "fakehashedpassword",
    }
}

def _get_user(username: str) -> User | None:
    user_data = _fake_users_db.get(username)
    if not user_data:
        return None
    return User(**user_data)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(token: str = Security(oauth2_scheme)) -> User:
    payload = verify_token(token)
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    user = _get_user(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user
