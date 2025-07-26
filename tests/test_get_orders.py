from utils.api_client import get_orders

def test_get_orders():
    response = get_orders()
    assert response.status_code == 200
    assert "orders" in response.json()
