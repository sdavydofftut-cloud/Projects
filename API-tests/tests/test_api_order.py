import allure
import pytest
from api.orders_client import OrdersClient
from data.constants import BASE_URL, MSG_INGREDIENTS_REQUIRED, INVALID_INGREDIENT_ID

@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrders:

    @allure.title("Создание заказа с авторизацией: 200 ОК")
    def test_create_order_with_auth_success(self, authorized_user, ingredient_ids):
        orders_client = OrdersClient(BASE_URL)
        raw_token = authorized_user["access_token"].replace("Bearer ", "")
        response = orders_client.create_order(
            ingredients=ingredient_ids[:2],
            access_token=raw_token)
        response_body = response.json()
        assert response.status_code == 200
        assert response_body.get("success") is True
        assert "order" in response_body
        assert "number" in response_body["order"]
        assert "name" in response_body

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_success(self, ingredient_ids):
        orders_client = OrdersClient(BASE_URL)
        response = orders_client.create_order(ingredient_ids[:2], access_token=None)
        assert response.status_code == 200

    @allure.title("Создание заказа с ингредиентами: разное количество ингредиентов (параметризация)")
    @pytest.mark.parametrize("count", [1, 2, 3])
    def test_create_order_with_ingredients_success(self, ingredient_ids, count):
        orders_client = OrdersClient(BASE_URL)
        response = orders_client.create_order(ingredient_ids[:count])
        response_body = response.json()
        assert response.status_code == 200
        assert response_body.get("success") is True
        assert "order" in response_body
        assert "number" in response_body["order"]
        assert "name" in response_body

    @allure.title("Создание заказа без ингредиентов: 400 Bad Request")
    def test_create_order_without_ingredients_return_400(self):
        orders_client = OrdersClient(BASE_URL)
        response = orders_client.create_order(ingredients=[], access_token=None)
        response_body = response.json()
        assert response.status_code == 400
        assert response_body["message"] == MSG_INGREDIENTS_REQUIRED 
    
    @allure.title("Создание заказа с неверным хешем ингредиента: 500 Internal Server Error")
    def test_create_order_with_invalid_ingredient_return_500(self, authorized_user):
        orders_client = OrdersClient(BASE_URL)
        response = orders_client.create_order(
            ingredients=[INVALID_INGREDIENT_ID],
            access_token=authorized_user["access_token"])
        assert response.status_code == 500
