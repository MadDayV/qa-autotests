import logging

import allure
import requests

logger = logging.getLogger("api")


class ApiClient:
    def __init__(self, base_url: str, timeout: float = 15) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    @allure.step("GET {path}")
    def get(self, path: str) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.get(url, timeout=self.timeout)
        logger.info("GET %s -> %s", url, response.status_code)
        return response
