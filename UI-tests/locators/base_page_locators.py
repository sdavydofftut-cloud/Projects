from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, "//div[contains(@class, 'App_App')]//p[text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH, "//div[contains(@class, 'App_App')]//p[text()='Лента Заказов']")
