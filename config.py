"""Settings for public demo sites.

SauceDemo publishes standard_user and locked_out_user on its login page.
JSONPlaceholder does not require an API key.
"""

import os

# Local pytest opens the browser. GitHub Actions sets CI and stays headless.
# HEADED=0 hides the window on this machine too.
HEADED = os.getenv("HEADED", "0" if os.getenv("CI") else "1") == "1"

BASE_URL = "https://www.saucedemo.com"
API_URL = "https://jsonplaceholder.typicode.com"

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"

CHECKOUT_FIRST_NAME = "Alex"
CHECKOUT_LAST_NAME = "Kim"
CHECKOUT_POSTAL_CODE = "050000"

PRODUCT_NAME = "Sauce Labs Backpack"
PRODUCT_DESCRIPTION_SNIPPET = "carry.allTheThings()"
PRODUCTS_TITLE = "Products"
ORDER_COMPLETE_HEADER = "Thank you for your order!"

ERROR_WRONG_CREDENTIALS = (
    "Epic sadface: Username and password do not match any user in this service"
)
ERROR_PASSWORD_REQUIRED = "Epic sadface: Password is required"
ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
