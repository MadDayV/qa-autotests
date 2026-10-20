import allure

from pages.playwright.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    COMPLETE_HEADER = "xpath=//h2[@class='complete-header']"

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
