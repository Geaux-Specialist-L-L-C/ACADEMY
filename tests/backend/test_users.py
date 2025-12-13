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
from backend.services.user_service import get_password_hash

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


def create_user(db_session, username: str = "testuser", password: str = "secret"):
    repository = UserRepository(db_session)
    return repository.create(
        UserCreate(username=username, email=f"{username}@example.com", password=password),
        hashed_password=get_password_hash(password),
    )


def test_get_user_profile_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401  # Expect unauthorized without authentication


def test_get_user_profile_authorized(client, db_session):
    user = create_user(db_session)
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


def test_login_returns_access_token(client, db_session):
    create_user(db_session)

    response = client.post(
        "/token", data={"username": "testuser", "password": "secret"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]


def test_login_rejects_invalid_credentials(client, db_session):
    create_user(db_session)

    response = client.post(
        "/token", data={"username": "testuser", "password": "wrong"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect username or password"


def test_signup_creates_user(client, db_session):
    response = client.post(
        "/signup",
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "full_name": "New User",
            "password": "freshpass",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["username"] == "newuser"
    assert body["email"] == "newuser@example.com"

    repository = UserRepository(db_session)
    created = repository.get_by_username("newuser")
    assert created is not None
