import pytest
from data.courier_data import generate_courier
from utils.api_client import create_courier, delete_courier, login_courier

@pytest.fixture
def new_courier():
    courier = generate_courier()
    create_resp = create_courier(courier)
    assert create_resp.status_code == 201
    login_resp = login_courier({"login": courier["login"], "password": courier["password"]})
    courier_id = login_resp.json()["id"]
    yield courier, courier_id
    delete_courier(courier_id)
