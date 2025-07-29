import allure
from utils.api_client import get_order_by_track, create_order


class TestGetOrderByTrack:
    @allure.title("Получение заказа по трек-номеру")
    def test_get_order_by_valid_track(self, created_order):
        with allure.step("Получить заказ по валидному треку"):
            response = get_order_by_track(created_order["track"])

        with allure.step("Проверить данные заказа"):
            assert response.status_code == 200
            order = response.json()["order"]
            assert "id" in order
            assert order["status"] in ("OPEN", "IN_PROGRESS", "COMPLETED")
            assert "courierId" in order  # Согласно документации API

    @allure.title("Получение заказа по несуществующему треку")
    def test_get_order_by_invalid_track(self):
        with allure.step("Попытаться получить заказ по невалидному треку"):
            response = get_order_by_track(9999999)

        with allure.step("Проверить ошибку 'Заказ не найден'"):
            assert response.status_code == 404
            assert response.json()["message"] == "Заказ не найден"

    @allure.title("Получение заказа без указания трека")
    def test_get_order_without_track(self):
        with allure.step("Попытаться получить заказ без трека"):
            response = get_order_by_track(None)

        with allure.step("Проверить ошибку валидации"):
            assert response.status_code == 400
            assert "Недостаточно данных" in response.json()["message"]