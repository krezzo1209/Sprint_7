from data.courier_data import generate_courier
from utils.api_client import create_courier

def test_create_courier_success():
    courier = generate_courier()
    response = create_courier(courier)
    assert response.status_code == 201
    assert response.json()["ok"] is True
