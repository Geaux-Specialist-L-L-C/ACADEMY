from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
