import allure
from utils.api_client import get_orders, create_order


class TestGetOrders:
    @allure.title("Получение списка заказов")
    def test_get_orders(self):
        with allure.step("Получить список заказов"):
            response = get_orders()

        with allure.step("Проверить структуру ответа"):
            assert response.status_code == 200
            response_json = response.json()
            assert "orders" in response_json
            assert isinstance(response_json["orders"], list)

            if response_json["orders"]:
                order = response_json["orders"][0]
                assert all(field in order for field in ["id", "status", "courierId", "createdAt"])

    @allure.title("Получение списка заказов после создания нового")
    def test_get_orders_after_creation(self, created_order):
        with allure.step("Получить список заказов"):
            response = get_orders()

        with allure.step("Проверить наличие созданного заказа"):
            assert response.status_code == 200
            orders = response.json()["orders"]
            assert any(order["id"] == created_order["order_id"] for order in orders)