import allure
import requests
from api.base_client import BaseClient
from api.endpoints import AUTH_REGISTER, AUTH_LOGIN, AUTH_USER

class UserClient(BaseClient):
    @allure.step("Регистрируем пользователя")
    def register(self, payload: dict) -> requests.Response:
        return self.request("POST", AUTH_REGISTER, json=payload)

    @allure.step("Авторизуемся под  пользователем")
    def login(self, payload: dict) -> requests.Response:
        return self.request("POST", AUTH_LOGIN, json=payload)
        
    @allure.step("Удаляем пользователя")
    def delete_user(self, access_token: str) -> requests.Response:
        headers = {"Authorization": f"Bearer {access_token}"}
        return self.request("DELETE", AUTH_USER, headers=headers)
