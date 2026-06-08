import allure
from api.user_client import UserClient
from data.constants import BASE_URL, MSG_INVALID_CREDENTIALS

@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user_success(self, registered_user):
        client = UserClient(BASE_URL)
        response = client.login(
            {
                "email": registered_user["email"],
                "password": registered_user["password"],
            }
        )
        response_body = response.json()
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response_body
        assert "refreshToken" in response_body

    @allure.title("Вход с неверным логином и/или паролем")
    def test_login_wrong_credentials_returns_error(self):
        client = UserClient(BASE_URL)
        response = client.login({"email": "no_such_user@yandex.ru", "password": "wrongpass"})
        response_body = response.json()
        assert response.status_code == 401
        assert response_body.get("success") is False
        assert response_body["message"] == MSG_INVALID_CREDENTIALS
