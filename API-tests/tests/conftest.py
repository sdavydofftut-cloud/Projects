import pytest
from data.constants import BASE_URL
from api.user_client import UserClient
from api.ingredient_client import IngredientsClient
from helpers.user_generate_data import build_new_user_payload

@pytest.fixture(scope="function")
def cleanup_users():
    client = UserClient(BASE_URL)
    tokens = []
    credentials = []

    def _register_for_cleanup(*, access_token=None, email=None, password=None):
        if access_token:
            tokens.append(access_token)
        elif email and password:
            credentials.append((email, password))
    
    yield _register_for_cleanup 

    for token in tokens:
        try:
            client.delete_user(token)
        except Exception as e:
            print(f"Ошибка при удалении пользователя по токену: {e}")

    for email, password in credentials:
        try:
            response_login = client.login({"email": email, "password": password})
            if response_login.status_code == 200:
                access_token = response_login.json().get("accessToken")
                if access_token:
                    client.delete_user(access_token)
        except Exception as e:
            print(f"Ошибка при удалении пользователя по email/pass: {e}")

@pytest.fixture(scope="function")
def registered_user(cleanup_users):
    client = UserClient(BASE_URL)
    payload = build_new_user_payload()
    response = client.register(payload)
    response_body = response.json()
    access_token = response_body.get("accessToken")# or body.get("access_token")
    if access_token:
        cleanup_users(access_token=access_token)
    elif payload.get("email") and payload.get("password"):
        cleanup_users(email=payload["email"], password=payload["password"])
    return payload

@pytest.fixture(scope="function")
def authorized_user(registered_user):
    client = UserClient(BASE_URL)
    response_login = client.login(
        {
            "email": registered_user["email"],
            "password": registered_user["password"],
        }
    )
    response_body = response_login.json()
    
    return {
        "email": registered_user["email"],
        "password": registered_user["password"],
        "access_token": response_body.get("accessToken") or response_body.get("access_token"),
        "response": response_login,
    }

@pytest.fixture
def ingredient_ids():
    client = IngredientsClient(BASE_URL)
    response = client.get_ingredients()
    response_body = response.json()
    return [item["_id"] for item in response_body["data"]]
