import allure
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from curl import BASE_URL
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators

class MainPage(BasePage):

    @allure.step(f"Открываем приложение Stellar Burger: {BASE_URL}")
    def main_open(self, base_url):
        self.open(base_url)

    @allure.step("Переходим на страницу Ленты заказов")
    def transfer_to_order_feed(self):
        with allure.step("C главной страницы переходим в Ленту заказов по клику на надпись"):
            self.find(BasePageLocators.BUTTON_ORDER_FEED)
            self.js_click(BasePageLocators.BUTTON_ORDER_FEED)
        with allure.step("Фиксируем переход на страницу Лента заказов: в URL довален '/feed'"):
            self.wait_url_contains("/feed")
    
    @allure.step("Переходим на страницу Конструктора")
    def transfer_to_constructor(self):
        with allure.step("С главной страницы переходим в Ленту заказов по клику на надпись"):
            self.find(BasePageLocators.BUTTON_ORDER_FEED)
            self.js_click(BasePageLocators.BUTTON_ORDER_FEED)
        with allure.step("Со страницы Ленты заказаов переходим на страницу Конструктора по по клику на надпись"):
            self.js_click(BasePageLocators.BUTTON_CONSTRUCTOR)
            self.element_visible(MainPageLocators.TEXT_ASSEMBLE_BURGER)

    @allure.step("На странице Конструктора кликаем на ингредиент, ждём появления окна с его делатями")
    def ingredient_detail_window_appears(self):
        self.find_visible(MainPageLocators.IMAGE_ROLLS_R2D3)
        self.js_click(MainPageLocators.IMAGE_ROLLS_R2D3)
        self.find_visible(MainPageLocators.WINDOW_DETAIL_ING)

    @allure.step("На странице Конструктора кликаем на ингредиент, ждём появления окна с его делатями, в окне с деталями кликаем на крестик")
    def ingredient_detail_window_closes(self):
        self.find_visible(MainPageLocators.IMAGE_ROLLS_R2D3)
        self.js_click(MainPageLocators.IMAGE_ROLLS_R2D3)
        self.click(MainPageLocators.BUTTON_CLOSE_WINDOW_DETAIL_ING)

    @allure.step("Фиксируем количество ингредиента в счётчике")
    def get_count_before_add_ingredient(self):
        order = self.element_visible(MainPageLocators.THIS_INGREDIENT)
        try:
            count = order.find_element(*MainPageLocators.COUNTER)
            text = count.text.strip()
            return int(text) if text else 0
        except NoSuchElementException:
            return 0

    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_in_order(self):
        SOURCE = MainPageLocators.INGREDIENT
        ZONE = MainPageLocators.DROP_ZONE_BASCETLIST
        try:
            self.drag_and_drop(SOURCE, ZONE)
        except Exception as e:
            print(f"[ERROR] Не удалось добавить ингредиент: {e}")
            raise

    @allure.step("Ждём изменение значения счётчика")
    def wait_counter_change(self, value: int):
        self.wait.until(lambda driver: self.get_count_before_add_ingredient() == value)

    @allure.step("Добавляем булочку в конструктор")
    def add_duble_roll_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.IMAGE_ROLLS_R2D3,
            MainPageLocators.DROP_ZONE_BASCETLIST,
        )
        self.drag_and_drop(
            MainPageLocators.IMAGE_ROLLS_R2D3,
            MainPageLocators.DROP_ZONE_BASCETLIST,
        )

    @allure.step("Кликаем 'Войти в аккаунт'")
    def click_button_login_accaunt(self):
        self.js_click(LoginPageLocators.BUTTON_LOGIN_ACCAUNT)

    @allure.step("Кликаем 'Войти'")
    def click_button_login(self):
        self.click(LoginPageLocators.BUTTON_LOGIN)

    @allure.step("Кликаем 'Оформить заказ'")
    def click_place_order(self):
        self.js_click(MainPageLocators.BUTTON_ORDER_PLACE)

    @allure.step("Фиксируем номер заказа")
    def get_order_number(self) -> str:
        text = self.get_text(MainPageLocators.ORDER_NUMBER)
        return "".join(symbol for symbol in text if symbol.isdigit())

    @allure.step("Ждём появления окна с номером заказа")
    def wait_window_order_number(self):
        self.find_visible(MainPageLocators.WINDOW_ORDER_NUMBER)
