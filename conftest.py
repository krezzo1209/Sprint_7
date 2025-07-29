import pytest
import allure
from utils.api_client import create_order, accept_order, finish_order


@pytest.fixture
def created_order():
    order_data = {
        "firstName": "Тест",
        "lastName": "Тестов",
        "address": "ул. Тестовая, 1",
        "metroStation": 204,  # ID согласно документации
        "phone": "+79991112233",
        "rentTime": 3,
        "deliveryDate": "2025-08-01",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }

    response = create_order(order_data)
    yield {"order_id": response.json()["track"]}  # track -> order_id в других эндпоинтах

    # Можно добавить отмену заказа при необходимости