import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helper import reg_user_by_api, delete_user_by_api

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1400,900")
        drv = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        drv = webdriver.Firefox(options=options)
        drv.set_window_size(1400, 900)
    yield drv
    drv.quit()

@pytest.fixture
def registered_user():
    user, response = reg_user_by_api()
    body = response.json() if response.content else {}
    access_token = body.get("accessToken")
    yield {
        "user": user,
        "response": response,
    }
    if access_token:
        delete_user_by_api(access_token)
