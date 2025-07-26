from utils.api_client import get_order_by_track

def test_get_order_by_invalid_track():
    response = get_order_by_track(9999999)
    assert response.status_code == 404
