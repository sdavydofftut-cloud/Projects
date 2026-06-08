from selenium.webdriver.common.by import By

class MainPageLocators:
    TEXT_ORDER_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]//h1[text()='Лента заказов']")
    TEXT_ASSEMBLE_BURGER = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]/h1[text()='Соберите бургер']")
    WINDOW_DETAIL_ING = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE_WINDOW_DETAIL_ING = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    IMAGE_ROLLS_R2D3 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    BUTTON_ORDER_PLACE = (By.XPATH, "//button[.//span[normalize-space()='Оформить заказ'] or normalize-space()='Оформить заказ']",)    
    INGREDIENT = (By.XPATH, "(//h2[normalize-space()='Соусы']/following::*//a[contains(@href,'/ingredient/')])[1]",)
    THIS_INGREDIENT = INGREDIENT
    COUNTER = (By.XPATH, ".//p[contains(@class,'counter') or contains(@class,'Counter')]",)
    DROP_ZONE_BASCETLIST = (By.XPATH, "//*[contains(@class,'BurgerConstructor')]",)
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class,'digits') or contains(@class,'Digits') or contains(@class,'Modal_modal__title')]",)
    WINDOW_ORDER_NUMBER = (By.XPATH, "//section[contains(@class,'Modal_modal') or contains(@class,'Modal')]",)
    