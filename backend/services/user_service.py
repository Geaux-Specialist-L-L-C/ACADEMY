"""Domain services for User-related operations."""

from passlib.context import CryptContext

from backend.repositories.user_repository import UserRepository
from backend.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Generate a secure hash for the given plaintext password."""

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against its hashed counterpart."""

    return pwd_context.verify(plain_password, hashed_password)


class UserService:
    """Business logic for users."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_by_username(self, username: str):
        return self.repository.get_by_username(username)

    def create_user(self, user_create: UserCreate):
        hashed_password = get_password_hash(user_create.password)
        return self.repository.create(user_create, hashed_password)

    def authenticate_user(self, username: str, password: str):
        user = self.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
