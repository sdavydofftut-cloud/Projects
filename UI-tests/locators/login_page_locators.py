from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' or @type='password']")
    BUTTON_LOGIN = (By.XPATH, "//button[.//span[normalize-space()='Войти'] or normalize-space()='Войти']")
    BUTTON_LOGIN_ACCAUNT = (By.XPATH, "//button[.//span[normalize-space()='Войти в аккаунт'] or normalize-space()='Войти в аккаунт']",)
