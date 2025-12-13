"""Domain services for User-related operations."""

from passlib.context import CryptContext

from backend.repositories.user_repository import UserRepository
from backend.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


class UserService:
    """Business logic for users."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_by_username(self, username: str):
        return self.repository.get_by_username(username)

    def create_user(self, user_create: UserCreate):
        hashed_password = get_password_hash(user_create.password)
        return self.repository.create(user_create, hashed_password)
