import allure
import pytest

from config import PRODUCT_DESCRIPTION_SNIPPET

pytestmark = [allure.feature("Selenium UI"), allure.story("Inventory")]


@pytest.mark.regression
def test_backpack_description_text(inventory_page):
    assert PRODUCT_DESCRIPTION_SNIPPET in inventory_page.backpack_description()
