# File: /geaux-academy/geaux-academy/tests/backend/test_users.py
# Description: Unit tests for user-related API endpoints.
# Author: [Your Name]
# Created: [Date]

from fastapi.testclient import TestClient
from backend.main import app  # Adjust the import based on your main FastAPI app file
from backend.models.user import User
from backend.auth.jwt_handler import create_access_token

client = TestClient(app)

def test_get_user_profile_unauthorized():
    response = client.get("/users/me")
    assert response.status_code == 401  # Expect unauthorized without authentication

def test_get_user_profile_authorized():
    # Assuming you have a way to create a test user and get a token
    test_user = User(username="testuser", email="test@example.com")
    token = create_access_token(data={"sub": test_user.username})
    
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"username": test_user.username, "email": test_user.email}  # Adjust based on your User schema