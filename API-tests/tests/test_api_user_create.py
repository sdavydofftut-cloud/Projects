import allure
import pytest
from api.user_client import UserClient
from helpers.user_generate_data import build_new_user_payload
from data.payload_templates import USER_MISSING_REQUIRED_FIELD
from data.constants import BASE_URL, MSG_USER_EXISTS, MSG_MISSING_FIELDS

@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestUserCreate:

    @allure.title("Cоздаётся уникальный пользователь")
    def test_register_unique_user_success(self, cleanup_users):
        client = UserClient(BASE_URL)
        payload = build_new_user_payload()
        response = client.register(payload)
        response_body = response.json()
        assert response.status_code == 200
        assert response_body.get("success") is True
        assert "accessToken" in response_body
        assert response_body["user"]["email"] == payload["email"]
        assert response_body["user"]["name"] == payload["name"]
        access_token = response_body.get("accessToken")
        if access_token:
            cleanup_users(access_token=access_token)

    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    def test_register_existing_user_returns_error(self, registered_user):
        client = UserClient(BASE_URL)
        response = client.register(registered_user)
        response_body = response.json()
        assert response.status_code == 403
        assert response_body.get("success") is False
        assert response_body["message"] == MSG_USER_EXISTS
    
    @allure.title("Отсутствие обязательных полей при регистрации возвращает ошибку 403")
    @pytest.mark.parametrize("missing_field, bad_payload", USER_MISSING_REQUIRED_FIELD)
    def test_register_missing_required_field_return_4xx(
        self,
        missing_field,
        bad_payload,
        cleanup_users,
    ):
        client = UserClient(BASE_URL)
        payload = build_new_user_payload()
        payload.update(bad_payload)
        if missing_field in payload:
            payload.pop(missing_field)
        if payload.get("email") and payload.get("password"):
            cleanup_users(email=payload["email"], password=payload["password"])
        response = client.register(payload)
        response_body = response.json()
        assert response.status_code == 403
        assert response_body.get("success") is False
        assert response_body["message"] == MSG_MISSING_FIELDS
