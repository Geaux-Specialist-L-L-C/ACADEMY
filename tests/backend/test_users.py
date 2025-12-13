# File: /geaux-academy/geaux-academy/tests/backend/test_users.py
# Description: Unit tests for user-related API endpoints.
# Author: [Your Name]
# Created: [Date]

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.auth.jwt_handler import create_access_token
from backend.database import get_db
from backend.main import app
from backend.models.user import Base
from backend.repositories.user_repository import UserRepository
from backend.schemas.user import UserCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_get_user_profile_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401  # Expect unauthorized without authentication


def test_get_user_profile_authorized(client, db_session):
    repository = UserRepository(db_session)
    user = repository.create(
        UserCreate(username="testuser", email="test@example.com", password="secret"),
        hashed_password="hashedsecret",
    )
    token = create_access_token(data={"sub": user.username})

    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "full_name": None,
        "is_active": True,
    }
