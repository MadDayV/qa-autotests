import allure
from selenium.webdriver.common.by import By

from pages.selenium.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE = (By.CSS_SELECTOR, "#continue")
    FINISH = (By.CSS_SELECTOR, "#finish")
    COMPLETE_HEADER = (By.XPATH, "//h2[@class='complete-header']")

    def wait_for_customer_form(self) -> None:
        self.wait_for(self.FIRST_NAME)

    @allure.step("Fill checkout information")
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    @allure.step("Finish checkout")
    def finish(self) -> None:
        self.wait_for(self.FINISH)
        self.click(self.FINISH)

    def complete_header(self) -> str:
        return self.text_of(self.COMPLETE_HEADER)
