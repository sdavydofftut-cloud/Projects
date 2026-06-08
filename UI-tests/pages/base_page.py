from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.find(locator).click()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_visible(self, locator):
        self.find_visible(locator).click()

    def find_clicable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_clicable(self, locator):
        self.find_clicable(locator).click()

    def set_text(self, locator, value: str):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def wait_text_in_element(self, locator, value: str):
        return self.wait.until(EC.text_to_be_present_in_element(locator, value))

    def get_text(self, locator):
        return self.find_visible(locator).text

    def get_attribute_value(self, locator, attribute_name):
        return self.find(locator).get_attribute(attribute_name)  

    def element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_url_contains(self, value):
        return self.wait.until(EC.url_contains(value))
    
    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False    

    def is_element_disappeared(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop(self, source_locator, target_locator):
            element_from_list = self.driver.find_elements(*source_locator)
            element_to_list = self.driver.find_elements(*target_locator)
            if not element_from_list or not element_to_list:
                print("[WARN] Один из элементов для DnD не найден.")
                return
            element_from = element_from_list[0]
            element_to = element_to_list[0]
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_from)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_to)
            js_code = """
                var source = arguments[0];
                var target = arguments[1];
                // Создаем объект dataTransfer, это ОБЯЗАТЕЛЬНО для HTML5 DnD
                var dataTransfer = {
                    data: {},
                    setData: function(type, val) { this.data[type] = val; },
                    getData: function(type) { return this.data[type]; },
                    dropEffect: 'copy', // или 'move'
                    effectAllowed: 'copy' // или 'move'
                };
                // Создаем и вызываем современные события
                var createEvent = function(eventName) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(eventName, true, true, null);
                    event.dataTransfer = dataTransfer;
                    return event;
                };
                source.dispatchEvent(createEvent('dragstart'));
                target.dispatchEvent(createEvent('dragenter'));
                target.dispatchEvent(createEvent('dragover'));
                target.dispatchEvent(createEvent('drop'));
                source.dispatchEvent(createEvent('dragend'));
                console.log('JS_DND: События отправлены');
            """
            self.driver.execute_script(js_code, element_from, element_to)
