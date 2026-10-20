import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Open {url}")
    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="load")

    @allure.step("Click {locator}")
    def click(self, locator: str) -> None:
        self.page.locator(locator).click()

    @allure.step("Fill {locator}")
    def fill(self, locator: str, value: str) -> None:
        self.page.locator(locator).fill(value)

    @allure.step("Wait for {locator}")
    def wait_for(self, locator: str) -> None:
        self.page.locator(locator).wait_for(state="visible")

    @allure.step("Wait until {locator} is hidden")
    def wait_hidden(self, locator: str) -> None:
        self.page.locator(locator).wait_for(state="hidden")

    def text_of(self, locator: str) -> str:
        self.wait_for(locator)
        return self.page.locator(locator).inner_text().strip()
