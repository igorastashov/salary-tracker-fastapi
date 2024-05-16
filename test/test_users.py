from fastapi.testclient import TestClient


def test_register_user(client: TestClient):
    response = client.post(
        "/users",
        json={"email": "testuser@example.com", "password": "password"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data


def test_login_user(client: TestClient):
    # Зарегистрируем нового пользователя
    client.post(
        "/users",
        json={"email": "testuser@example.com", "password": "password"}
    )
    # Получим токен
    response = client.post(
        "/tokens",
        json={"email": "testuser@example.com", "password": "password"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert "expires_at" in data
