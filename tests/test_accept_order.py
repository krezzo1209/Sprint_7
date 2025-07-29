import allure
from utils.api_client import accept_order


class TestAcceptOrder:
    @allure.title("Принятие заказа курьером")
    def test_accept_order_success(self, created_order, registered_courier):
        with allure.step("Принять заказ валидным курьером"):
            response = accept_order(
                order_id=created_order["order_id"],
                courier_id=registered_courier["courier_id"]
            )

        with allure.step("Проверить успешное выполнение запроса"):
            assert response.status_code == 200
            assert response.json() == {"ok": True}

    @allure.title("Принятие несуществующего заказа")
    def test_accept_invalid_order(self, registered_courier):
        with allure.step("Попытаться принять несуществующий заказ"):
            response = accept_order(
                order_id=999999,
                courier_id=registered_courier["courier_id"]
            )

        with allure.step("Проверить ошибку 'Заказ не найден'"):
            assert response.status_code == 404
            assert response.json()["message"] == "Заказ не найден"