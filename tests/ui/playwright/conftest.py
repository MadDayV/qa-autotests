from pathlib import Path

import allure
import pytest
from playwright.sync_api import sync_playwright

from config import HEADED, PASSWORD, STANDARD_USER
from pages.playwright.inventory_page import InventoryPage
from pages.playwright.login_page import LoginPage

VIDEOS_DIR = Path(__file__).resolve().parents[3] / "videos"


@pytest.fixture
def page(request):
    VIDEOS_DIR.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        # Full Chromium keeps text in the recording. --headless=new hides the window.
        launch_args = [] if HEADED else ["--headless=new"]
        browser = playwright.chromium.launch(headless=False, args=launch_args)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir=VIDEOS_DIR,
            record_video_size={"width": 1280, "height": 720},
        )
        browser_page = context.new_page()
        browser_page.set_default_timeout(15_000)
        yield browser_page
        try:
            browser_page.wait_for_timeout(1000)
        finally:
            video_path = browser_page.video.path()
            context.close()
            browser.close()
            request.node.playwright_video = video_path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    video_path = getattr(item, "playwright_video", None)
    if report.when == "teardown" and video_path and Path(video_path).is_file():
        allure.attach.file(
            video_path,
            name="recording",
            attachment_type=allure.attachment_type.WEBM,
        )


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def inventory_page(login_page):
    login_page.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(login_page.page)
    inventory.wait_until_opened()
    return inventory
