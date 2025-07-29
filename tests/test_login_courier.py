import allure
import pytest
from utils.api_client import login_courier


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, registered_courier):
        with allure.step("Авторизоваться валидными данными"):
            response = login_courier({
                "login": registered_courier["login"],
                "password": registered_courier["password"]
            })

        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "id" in response.json()
            assert isinstance(response.json()["id"], int)

    @allure.title("Авторизация с неверными данными")
    @pytest.mark.parametrize("invalid_data,expected_message", [
        ({"login": "invalid", "password": "invalid"}, "Учетная запись не найдена"),
        ({"login": "", "password": "any"}, "Недостаточно данных"),
        ({"login": "valid", "password": ""}, "Недостаточно данных"),
        ({}, "Недостаточно данных")
    ])
    def test_login_invalid_credentials(self, invalid_data, expected_message):
        with allure.step("Попытаться авторизоваться с невалидными данными"):
            response = login_courier(invalid_data)

        with allure.step("Проверить соответствующую ошибку"):
            assert response.status_code in (404, 400)
            assert expected_message in response.json()["message"]