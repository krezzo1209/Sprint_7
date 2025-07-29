import allure
from utils.api_client import delete_courier


class TestDeleteCourier:
    @allure.title("Удаление существующего курьера")
    def test_delete_existing_courier(self, registered_courier):
        with allure.step("Удалить существующего курьера"):
            response = delete_courier(registered_courier["courier_id"])

        with allure.step("Проверить успешное удаление"):
            assert response.status_code == 200
            assert response.json() == {"ok": True}

    @allure.title("Удаление несуществующего курьера")
    def test_delete_non_existing_courier(self):
        with allure.step("Попытаться удалить несуществующего курьера"):
            response = delete_courier(999999)

        with allure.step("Проверить ошибку 'Курьер не найден'"):
            assert response.status_code == 404
            assert response.json()["message"] == "Курьер с идентификатором 999999 не найден"

    @allure.title("Удаление курьера без ID")
    def test_delete_courier_without_id(self):
        with allure.step("Попытаться удалить курьера без ID"):
            response = delete_courier(None)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
            assert "Недостаточно данных" in response.json()["message"]