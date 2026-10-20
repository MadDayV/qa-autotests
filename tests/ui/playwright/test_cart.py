import allure
import pytest

from config import PRODUCT_NAME

pytestmark = [allure.feature("Playwright UI"), allure.story("Cart")]


@pytest.mark.regression
def test_add_backpack_to_cart(inventory_page):
    inventory_page.add_backpack()
    assert inventory_page.cart_badge() == "1"
    cart = inventory_page.open_cart()
    assert cart.item_name() == PRODUCT_NAME


@pytest.mark.regression
def test_remove_backpack_from_cart(inventory_page):
    inventory_page.add_backpack()
    cart = inventory_page.open_cart()
    cart.remove_backpack()
    assert cart.item_names() == []
    assert cart.badge_is_visible() is False
