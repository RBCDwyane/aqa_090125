import pytest
import requests

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_token():
    auth = ("test_user", "test_pass")
    response = requests.post(f"{BASE_URL}/auth", auth=auth)
    assert response.status_code == 200, "Не вдалося отримати токен!"
    return response.json()["access_token"]

