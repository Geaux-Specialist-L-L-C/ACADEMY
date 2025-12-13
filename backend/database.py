"""Database configuration and session management for the backend API."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.models.user import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Create database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Yield a database session for FastAPI dependency injection."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
