import allure

from pages.playwright.base_page import BasePage
from pages.playwright.cart_page import CartPage


class InventoryPage(BasePage):
    TITLE = "xpath=//span[@class='title']"
    ADD_BACKPACK = "button[data-test='add-to-cart-sauce-labs-backpack']"
    CART_LINK = "a.shopping_cart_link"
    CART_BADGE = "span.shopping_cart_badge"
    BACKPACK_DESCRIPTION = (
        "xpath=//div[contains(@class,'inventory_item_name') and normalize-space()='Sauce Labs Backpack']"
        "/ancestor::div[contains(@class,'inventory_item_description')]"
        "//div[contains(@class,'inventory_item_desc')]"
    )

    def wait_until_opened(self) -> None:
        self.wait_for(self.TITLE)

    def title(self) -> str:
        return self.text_of(self.TITLE)

    @allure.step("Add Sauce Labs Backpack to the cart")
    def add_backpack(self) -> None:
        self.click(self.ADD_BACKPACK)

    def cart_badge(self) -> str:
        return self.text_of(self.CART_BADGE)

    def backpack_description(self) -> str:
        return self.text_of(self.BACKPACK_DESCRIPTION)

    @allure.step("Open the cart")
    def open_cart(self) -> CartPage:
        self.click(self.CART_LINK)
        cart = CartPage(self.page)
        cart.wait_until_opened()
        return cart
