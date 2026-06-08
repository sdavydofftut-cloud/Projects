import allure
from pages.base_page import BasePage
from locators.reg_page_locators import RegPageLocators

class RegisterPage(BasePage):
    @allure.step("Ввести имя")
    def set_name(self, name: str):
        el = self.find_visible(RegPageLocators.NAME_INPUT)
        el.clear()
        el.send_keys(name)

    @allure.step("Ввести email")
    def set_email(self, email: str):
        el = self.find_visible(RegPageLocators.EMAIL_INPUT)
        el.clear()
        el.send_keys(email)

    @allure.step("Ввести пароль")
    def set_password(self, password: str):
        el = self.find_visible(RegPageLocators.PASSWORD_INPUT)
        el.clear()
        el.send_keys(password)

    @allure.step("Нажать 'Зарегистрироваться'")
    def push(self):
        self.click(RegPageLocators.BUTTON_REG)
        