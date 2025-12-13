# File: /backend/auth/jwt_handler.py
# Description: Functions for handling JWT authentication, including generating and verifying tokens.
# Author: [Your Name]
# Created: [Date]

import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer

from backend.models.user import User

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
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
