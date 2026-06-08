import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from curl import BASE_URL

class TestBaseFunction:

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_transfer_to_order_feed(self, driver):
        order_feed = MainPage(driver)
        order_feed.main_open(BASE_URL)
        order_feed.transfer_to_order_feed()
        with allure.step("Проверяем, что находимся на странице Лента заказов"):
            assert order_feed.is_displayed(MainPageLocators.TEXT_ORDER_FEED)

    @allure.title("Переход по клику на «Конструктор»")
    def test_transfer_to_constructor(self, driver):
        constructor = MainPage(driver)
        constructor.main_open(BASE_URL)
        constructor.transfer_to_constructor()
        with allure.step("Проверяем, что находимся на странице Конструктора"):
            assert constructor.is_displayed(MainPageLocators.TEXT_ASSEMBLE_BURGER)

    @allure.title("Появляется окно с деталями по клику на ингредиент")
    def test_ingredient_detail_window_appears(self, driver):
        window_ing = MainPage(driver)
        window_ing.main_open(BASE_URL)
        window_ing.ingredient_detail_window_appears()
        with allure.step("Проверяем, что окно на экране"):
            assert window_ing.is_displayed(MainPageLocators.WINDOW_DETAIL_ING)

    @allure.title("Окно с деталями закрывается по клику на крестик")
    def test_ingredient_detail_window_closes(self, driver):
        window_ing = MainPage(driver)
        window_ing.main_open(BASE_URL)
        window_ing.ingredient_detail_window_closes()
        with allure.step("Проверяем, что окно с деталями закрывается"):
            assert window_ing.is_element_disappeared(MainPageLocators.WINDOW_DETAIL_ING)

    @allure.title("При добавлении ингредиента счетчик увеличивается")
    def test_counter_up_by_add_ingredient(self, driver):
        with allure.step("Открываем гласную страницу с конструктором {{BASE_URL}}"):
            counter = MainPage(driver)
            counter.main_open(BASE_URL)
        with allure.step("Фиксируем значение счётчика ингредиента"):
            count_before = counter.get_count_before_add_ingredient()
        with allure.step("Перетаскиваем этот ингредиент в конструктор справа"):
            counter.add_ingredient_in_order()
        with allure.step("Фиксируем значение счётчика ингредиента после его добавления в конструктор"):
            counter.wait_counter_change(count_before + 1)
            count_after = counter.get_count_before_add_ingredient()
        with allure.step("Протверяем увеличение счётчика добавленного ингредиента"):
            assert count_after == count_before + 1
