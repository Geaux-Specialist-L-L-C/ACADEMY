"""Authentication and registration endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.auth.jwt_handler import create_access_token
from backend.database import get_db
from backend.repositories.user_repository import UserRepository
from backend.schemas.user import User as UserSchema
from backend.schemas.user import UserCreate
from backend.services.user_service import UserService

router = APIRouter()


@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """Authenticate a user using the password grant and return a JWT access token."""

    repository = UserRepository(db)
    service = UserService(repository)
    user = service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def signup(user_create: UserCreate, db: Session = Depends(get_db)):
    """Register a new user if the username does not already exist."""

    repository = UserRepository(db)
    service = UserService(repository)
    existing_user = service.get_by_username(user_create.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    user = service.create_user(user_create)
    return user
