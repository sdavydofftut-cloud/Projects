import allure
import requests
from api.base_client import BaseClient
from api.endpoints import ORDERS

class OrdersClient(BaseClient):
    @allure.step("Создаём заказ")
    def create_order(self, ingredients: list, access_token: str | None = None) -> requests.Response:
        headers = {}
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        payload = {"ingredients": ingredients}
        return self.request("POST", ORDERS, headers=headers or None, json=payload)
