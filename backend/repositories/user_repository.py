"""Data access layer for User entities."""

from sqlalchemy.orm import Session

from backend.models.user import User
from backend.schemas.user import UserCreate


class UserRepository:
    """Encapsulates User persistence operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()

    def create(self, user_create: UserCreate, hashed_password: str) -> User:
        user = User(
            username=user_create.username,
            email=user_create.email,
            full_name=getattr(user_create, "full_name", None),
            hashed_password=hashed_password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
