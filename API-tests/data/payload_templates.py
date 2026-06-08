USER_VALID_TEMPLATE: dict[str, str] = {
    "email": "TestBuger@ya.ru",
    "password": "StrongPasswordBurger!",
    "name": "BurgerUser",
}

USER_MISSING_REQUIRED_FIELD: list[tuple[str, dict[str, str]]] = [
    ("email", {"password": "not_a_strong_password", "name": "NoName"}),
    ("password", {"email": "some_kind@ya.ru", "name": "NoName"}),
    ("name", {"email": "some_kind@ya.ru", "password": "not_a_strong_password"}),
]
