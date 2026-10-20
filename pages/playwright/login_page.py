import allure

from config import BASE_URL
from pages.playwright.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR = "xpath=//h3[@data-test='error']"

    @allure.step("Open the login page")
    def open(self) -> None:
        super().open(BASE_URL)

    @allure.step("Log in as {username}")
    def login(self, username: str, password: str) -> None:
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_text(self) -> str:
        return self.text_of(self.ERROR)
