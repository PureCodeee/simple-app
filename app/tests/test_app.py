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


def test_get_users():
    response = client.get("/api/users/")

    assert response.status_code == 200

    data = response.json()

    assert data["users"][0]["id"] == 1
    assert data["users"][0]["name"] == "genesis_user"


def test_create_user():
    response = client.post("/api/users/", json={"name": "new_user"})

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 2
    assert data["name"] == "new_user"
    assert len(users) == 2
    assert users[-1].id == 2
    assert users[-1].name == "new_user"


def test_create_user_validation():
    response = client.post(
        "/api/users/",
        json={}
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data


def test_get_user():
    response = client.get("/api/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "genesis_user"


def test_get_user_not_found():
    response = client.get("/api/users/9999")

    assert response.status_code == 404


def test_delete_user():
    response = client.delete("/api/users/1")

    assert response.status_code == 204
    assert len(users) == 0

    response = client.get("/api/users/1")

    assert response.status_code == 404



def test_delete_user_not_found():
    response = client.delete("/api/users/999")

    assert response.status_code == 404