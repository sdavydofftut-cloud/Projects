from selenium.webdriver.common.by import By

class RegPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    BUTTON_REG = (By.XPATH, "//button[contains(., 'Зарегистрироваться')]")
    