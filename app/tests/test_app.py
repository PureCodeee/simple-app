import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models import users, DEFAULT_USERS

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_users():
    users.clear()
    users.extend(DEFAULT_USERS.copy())


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, World!"
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }