import pytest
import requests
import logging

BASE_URL = "http://127.0.0.1:8080"

logging.basicConfig(filename="test_search.log", level=logging.INFO)

@pytest.mark.parametrize("sort_by, limit", [
    ("brand", 5),
    ("year", 3),
    ("engine_volume", 10),
    ("price", 7),
    (None, None),
])
def test_get_cars_with_params(auth_token, sort_by, limit):
    headers = {"Authorization": f"Bearer {auth_token}"}
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = requests.get(f"{BASE_URL}/cars", headers=headers, params=params)

    logging.info(f"Запит: sort_by={sort_by}, limit={limit} — Код: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    if limit:
        assert len(data) <= limit
    if sort_by:
        values = [item[sort_by] for item in data]
        assert values == sorted(values), f"Сортування за {sort_by} не відбулось"
