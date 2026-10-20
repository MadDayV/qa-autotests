import allure
import pytest

from config import (
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
    ORDER_COMPLETE_HEADER,
)

pytestmark = [allure.feature("Playwright UI"), allure.story("Checkout")]


@pytest.mark.regression
def test_checkout_completes(inventory_page):
    inventory_page.add_backpack()
    cart = inventory_page.open_cart()
    checkout = cart.start_checkout()
    checkout.fill_customer_info(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE,
    )
    checkout.finish()
    assert checkout.complete_header() == ORDER_COMPLETE_HEADER
