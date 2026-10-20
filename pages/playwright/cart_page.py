import allure

from pages.playwright.base_page import BasePage
from pages.playwright.checkout_page import CheckoutPage


class CartPage(BasePage):
    ITEM_NAME = "xpath=//div[@class='inventory_item_name']"
    REMOVE_BACKPACK = "button[data-test='remove-sauce-labs-backpack']"
    CHECKOUT = "#checkout"
    CART_BADGE = "span.shopping_cart_badge"

    def wait_until_opened(self) -> None:
        self.wait_for(self.CHECKOUT)

    def item_name(self) -> str:
        return self.text_of(self.ITEM_NAME)

    def item_names(self) -> list[str]:
        return [text.strip() for text in self.page.locator(self.ITEM_NAME).all_inner_texts()]

    @allure.step("Remove Sauce Labs Backpack from the cart")
    def remove_backpack(self) -> None:
        self.click(self.REMOVE_BACKPACK)
        self.wait_hidden(self.ITEM_NAME)
        self.wait_hidden(self.CART_BADGE)

    def badge_is_visible(self) -> bool:
        return self.page.locator(self.CART_BADGE).is_visible()

    @allure.step("Start checkout")
    def start_checkout(self) -> CheckoutPage:
        self.click(self.CHECKOUT)
        checkout = CheckoutPage(self.page)
        checkout.wait_for_customer_form()
        return checkout
