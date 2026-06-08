import allure
from curl import BASE_URL
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.suite("Лента заказов")
class TestFeedFlow:

    @allure.title("После создания заказа увеличивается счетчик «Выполнено за всё время»")
    def test_total_counter_in_work_after_order_up(self, driver, registered_user):
        with allure.step("Регистрируемся"):
            user = registered_user["user"]
            assert registered_user["response"].status_code == 200
        with allure.step("Открывыем Ленту заказов, фиксируем количество заказов за всё время"):
            feed_orders = FeedPage(driver)
            feed_orders.open_feed()
            total_before = feed_orders.get_all_time_done()
        with allure.step("Открываем Конструктор, собираем бургер"):
            feed = MainPage(driver)
            feed.main_open(BASE_URL)
            feed.add_duble_roll_to_constructor()
            feed.add_ingredient_in_order()
            feed.click_button_login_accaunt()
        with allure.step("Авторизуемся"):
            login = LoginPage(driver)
            login.login(user.email, user.password)
        with allure.step("Клик по кнопке Оформить заказ, ждём окно с номером заказа"):
            feed.click_place_order()
            feed.wait_window_order_number()
        with allure.step("Открывыем Ленту заказов, фиксируем количество заказов за всё время"):
            feed_orders.open_feed()
            total_after = feed_orders.get_all_time_done()
        with allure.step("Проверяем, что количество заказов за всё время после оформленного заказа стало больше до его оформления"):
            assert total_after >= total_before

    @allure.title("После создания заказа увеличивается счетчик «Выполнено за сегодня»")
    def test_today_counter_increases_after_order(self, driver, registered_user):
        with allure.step("Регистрируемся"):
            user = registered_user["user"]
            assert registered_user["response"].status_code == 200
        with allure.step("Открывыем Ленту заказов, фиксируем фиксируем количество заказов за сегодня"):
            feed_orders = FeedPage(driver)
            feed_orders.open_feed()
            today_before = feed_orders.get_today_done()
        with allure.step("Открываем Конструктор, собираем бургер"):
            feed = MainPage(driver)
            feed.main_open(BASE_URL)
            feed.add_duble_roll_to_constructor()
            feed.add_ingredient_in_order()
            feed.click_button_login_accaunt()
        with allure.step("Авторизуемся"):
            login = LoginPage(driver)
            login.login(user.email, user.password)
        with allure.step("Клик по кнопке Оформить заказ, ждём окно с номером заказа"):
            feed.click_place_order()
            feed.wait_window_order_number()
        with allure.step("Открывыем Ленту заказов, фиксируем фиксируем количество заказов за сегодня"):
            feed_orders.open_feed()
            today_after = feed_orders.get_today_done()
        with allure.step("Проверяем, что количество заказов за сегодня после оформленного заказа стало больше до его оформления"):
            assert today_after >= today_before

    @allure.title("После создания заказа номер появляется в блоке «В работе»")
    def test_order_number_appears_in_work(self, driver, registered_user):
        with allure.step("Регистрируемся"):
            user = registered_user["user"]
            assert registered_user["response"].status_code == 200
        with allure.step("Открываем Конструктор, собираем бургер"):
            feed = MainPage(driver)
            feed.main_open(BASE_URL)
            feed.add_duble_roll_to_constructor()
            feed.add_ingredient_in_order()
            feed.click_button_login_accaunt()
        with allure.step("Авторизуемся"):
            login = LoginPage(driver)
            login.login(user.email, user.password)
        with allure.step("Клик по кнопке Оформить заказ, ждём окно с номером заказа, фиксируем номер заказа"):
            feed.click_place_order()
            feed.wait_window_order_number()
            order_number = feed.get_order_number()
        with allure.step("Открывыем Ленту заказов"):
            feed_orders = FeedPage(driver)
            feed_orders.open_feed()
        with allure.step("Проверяем, что в блоке 'В работе' есть номер созданного заказа"):
            assert feed_orders.is_order_in_work(order_number)
