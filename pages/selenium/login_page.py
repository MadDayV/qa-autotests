import allure
from selenium.webdriver.common.by import By

from config import BASE_URL
from pages.selenium.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR = (By.XPATH, "//h3[@data-test='error']")

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
