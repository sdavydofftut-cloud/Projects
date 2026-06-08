from dataclasses import dataclass
import random
import string
import requests
from curl import API_URL_FOR_DELETE_USER, API_URL_FOR_REG_USER

@dataclass(frozen=True)
class UserCredentials:
    email: str
    password: str
    name: str

def _rand(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

def reg_user_by_api():
    payload = {
        "email": f"{_rand()}@ya.ru",
        "password": f"&{_rand(6)}$",
        "name": f"User{_rand(4)}",
    }
    response = requests.post(
        API_URL_FOR_REG_USER,
        json=payload,
        timeout=20,
    )
    user = UserCredentials(
        email=payload["email"],
        password=payload["password"],
        name=payload["name"],
    )
    return user, response

def delete_user_by_api(access_token: str):
    return requests.delete(
        API_URL_FOR_DELETE_USER,
        headers={"Authorization": access_token},
        timeout=20,
    )

def reg_user():
    user, response = reg_user_by_api()
    body = response.json() if response.content else {}
    access_token = body.get("accessToken")
    yield {
        "user": user,
        "response": response,
    }
    if access_token:
        delete_user_by_api(access_token)
