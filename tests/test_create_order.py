import allure
import pytest
from utils.api_client import create_order


class TestCreateOrder:
    @allure.title("Создание заказа с разными комбинациями цветов")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_colors(self, order_data, color):
        with allure.step("Подготовить данные заказа"):
            test_data = order_data.copy()
            test_data["color"] = color

        with allure.step("Создать заказ"):
            response = create_order(test_data)

        with allure.step("Проверить корректность ответа"):
            assert response.status_code == 201
            response_json = response.json()
            assert "track" in response_json
            assert isinstance(response_json["track"], int)
            assert response_json["track"] > 0  # Проверка валидности трек-номера

    @allure.title("Создание заказа без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["firstName", "lastName", "address", "phone"])
    def test_create_order_missing_field(self, order_data, missing_field):
        with allure.step(f"Удалить обязательное поле {missing_field}"):
            invalid_data = order_data.copy()
            del invalid_data[missing_field]

        with allure.step("Попытаться создать заказ"):
            response = create_order(invalid_data)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
            assert "Недостаточно данных" in response.json()["message"]