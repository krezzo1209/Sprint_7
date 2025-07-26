import pytest
from utils.api_client import create_order

@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def test_create_order_with_colors(color):
    data = {
        "firstName": "Test",
        "lastName": "User",
        "address": "Test street",
        "metroStation": 4,
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2025-07-25",
        "comment": "Test order",
        "color": color
    }
    response = create_order(data)
    assert response.status_code == 201
    assert "track" in response.json()
