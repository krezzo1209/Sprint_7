import allure
import pytest
from utils.api_client import create_courier


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        with allure.step("Создать нового курьера"):
            response = create_courier(courier_data)

        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

    @allure.title("Создание дубликата курьера")
    def test_create_duplicate_courier(self, courier_data):
        with allure.step("Создать курьера первый раз"):
            create_courier(courier_data)

        with allure.step("Попытаться создать дубликат"):
            response = create_courier(courier_data)

        with allure.step("Проверить ошибку дубликата"):
            assert response.status_code == 409
            assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, courier_data, missing_field):
        with allure.step(f"Удалить обязательное поле {missing_field}"):
            invalid_data = courier_data.copy()
            del invalid_data[missing_field]

        with allure.step("Попытаться создать курьера"):
            response = create_courier(invalid_data)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"