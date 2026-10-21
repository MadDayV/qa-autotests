import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADED, PASSWORD, STANDARD_USER
from pages.selenium.inventory_page import InventoryPage
from pages.selenium.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    if not HEADED:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)
    if not HEADED:
        # Headless Chrome on Linux ignores --window-size. Set the layout viewport
        # directly, otherwise the cart link sits outside the clickable area.
        browser.execute_cdp_cmd(
            "Emulation.setDeviceMetricsOverride",
            {
                "width": 1920,
                "height": 1080,
                "deviceScaleFactor": 1,
                "mobile": False,
            },
        )
    yield browser
    if HEADED:
        time.sleep(1)
    browser.quit()


@pytest.fixture
def login_page(driver):
    login = LoginPage(driver)
    login.open()
    return login


@pytest.fixture
def inventory_page(login_page):
    login_page.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(login_page.driver)
    inventory.wait_until_opened()
    return inventory
