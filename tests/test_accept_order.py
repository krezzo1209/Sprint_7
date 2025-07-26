from utils.api_client import accept_order

def test_accept_order_with_invalid_ids():
    response = accept_order(order_id=99999, courier_id=99999)
    assert response.status_code == 404
