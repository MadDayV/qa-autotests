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
        # --window-size is ignored by headless Chrome on Linux CI, so clicks miss.
        browser.set_window_rect(width=1920, height=1080)
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
