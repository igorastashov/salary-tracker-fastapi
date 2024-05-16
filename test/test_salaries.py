from fastapi.testclient import TestClient


def test_read_salaries(client: TestClient):
    # Зарегистрируем и авторизуем пользователя
    client.post(
        "/users", json={"email": "testuser@example.com", "password": "password"}
    )
    response = client.post(
        "/tokens", json={"email": "testuser@example.com", "password": "password"}
    )
    token_data = response.json()

    # Добавим данные пользователя
    client.post(
        "/salaries",
        json={"amount": 5000, "next_raise_date": "2024-12-31T00:00:00"},
        headers={"Authorization": token_data["access_token"]},
    )

    # Прочтем данные о зарплате и следующем повышении пользователя
    response = client.get(
        "/salaries", headers={"Authorization": token_data["access_token"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["amount"] == 5000
    assert data[0]["next_raise_date"] == "2024-12-31T00:00:00"
