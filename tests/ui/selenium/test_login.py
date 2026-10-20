import allure
import pytest

from config import (
    ERROR_LOCKED_OUT,
    ERROR_PASSWORD_REQUIRED,
    ERROR_WRONG_CREDENTIALS,
    LOCKED_OUT_USER,
    PASSWORD,
    PRODUCTS_TITLE,
    STANDARD_USER,
)
from pages.selenium.inventory_page import InventoryPage

pytestmark = [allure.feature("Selenium UI"), allure.story("Login")]


@pytest.mark.smoke
def test_successful_login(login_page):
    login_page.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(login_page.driver)
    assert inventory.title() == PRODUCTS_TITLE


@pytest.mark.regression
@pytest.mark.parametrize(
    ("username", "password", "expected_error"),
    [
        pytest.param(
            STANDARD_USER,
            "wrong_password",
            ERROR_WRONG_CREDENTIALS,
            id="wrong-password",
        ),
        pytest.param(
            STANDARD_USER,
            "",
            ERROR_PASSWORD_REQUIRED,
            id="empty-password",
        ),
    ],
)
def test_login_rejected(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert login_page.error_text() == expected_error


@pytest.mark.regression
def test_locked_out_user_sees_error(login_page):
    login_page.login(LOCKED_OUT_USER, PASSWORD)
    assert login_page.error_text() == ERROR_LOCKED_OUT
