import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: float = 15) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Open {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Click {locator}")
    def click(self, locator: Locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )
        element.click()

    @allure.step("Fill {locator}")
    def fill(self, locator: Locator, value: str) -> None:
        element = self.wait_for(locator)
        element.clear()
        element.send_keys(value)

    @allure.step("Wait for {locator}")
    def wait_for(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Wait until {locator} is hidden")
    def wait_hidden(self, locator: Locator) -> None:
        self.wait.until(EC.invisibility_of_element_located(locator))

    def text_of(self, locator: Locator) -> str:
        return self.wait_for(locator).text.strip()
