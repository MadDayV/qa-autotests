# qa-autotests

Public portfolio demo of a Python test automation framework. Not a commercial product.

The same SauceDemo scenarios are implemented with Playwright and with Selenium. API checks use requests and Pydantic models.

## Stack

- Python 3.11
- pytest
- Playwright
- Selenium
- Pydantic
- requests
- Allure
- GitHub Actions

## Run tests

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS and Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest
```

Selenium uses the installed Google Chrome. Selenium Manager downloads the matching driver.

```bash
pytest tests/ui/playwright
pytest tests/ui/selenium
pytest tests/api
pytest -m smoke
```

## Allure

Install the Allure command line, then open the report from the project root:

```bash
allure serve allure-results
```

## CI

The workflow runs the full suite on Ubuntu with Python 3.11 and uploads the `allure-results` artifact:

https://github.com/MadDayV/qa-autotests/actions/workflows/tests.yml

## Author

David Madiyev, Almaty
