import allure
from curl import FEED_URL
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage

class FeedPage(BasePage):
    @allure.step(f"Открываем страницу Ленты заказов {FEED_URL}")    
    def open_feed(self):
        self.open(FEED_URL)
        self.find_visible(FeedPageLocators.FEED_HEADER)

    @allure.step("Фиксируем номер заказа в блоке 'В работе:'")    
    def is_order_in_work(self, order_number: str) -> bool:
        self.find_visible(FeedPageLocators.SECTION_IN_WORK)
        self.wait_text_in_element(FeedPageLocators.SECTION_IN_WORK, order_number)
        return order_number in self.get_text(FeedPageLocators.SECTION_IN_WORK)
    
    @allure.step("Фиксируем количество заказов за всё время")
    def get_all_time_done(self) -> int:
        return int(self.get_text(FeedPageLocators.ALL_TIME_DONE))

    @allure.step("Фиксируем количество заказов за сегодня")
    def get_today_done(self) -> int:
        return int(self.get_text(FeedPageLocators.TODAY_DONE))
    