import allure
from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage
from pages.selenium.checkout_page import CheckoutPage


class CartPage(BasePage):
    ITEM_NAME = (By.XPATH, "//div[@class='inventory_item_name']")
    REMOVE_BACKPACK = (By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
    CHECKOUT = (By.CSS_SELECTOR, "#checkout")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")

    def wait_until_opened(self) -> None:
        self.wait_for(self.CHECKOUT)

    def item_name(self) -> str:
        return self.text_of(self.ITEM_NAME)

    def item_names(self) -> list[str]:
        return [element.text.strip() for element in self.driver.find_elements(*self.ITEM_NAME)]

    @allure.step("Remove Sauce Labs Backpack from the cart")
    def remove_backpack(self) -> None:
        self.click(self.REMOVE_BACKPACK)
        self.wait_hidden(self.ITEM_NAME)
        self.wait_hidden(self.CART_BADGE)

    def badge_is_visible(self) -> bool:
        badges = self.driver.find_elements(*self.CART_BADGE)
        return bool(badges) and badges[0].is_displayed()

    @allure.step("Start checkout")
    def start_checkout(self) -> CheckoutPage:
        self.click(self.CHECKOUT)
        checkout = CheckoutPage(self.driver)
        checkout.wait_for_customer_form()
        return checkout
