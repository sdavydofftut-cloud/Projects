import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Заполняем поля Email и Password, клик по кнопке 'Войти'")
    def login(self, email: str, password: str):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.js_click(LoginPageLocators.BUTTON_LOGIN)
        