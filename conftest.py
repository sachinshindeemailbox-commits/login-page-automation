import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to use: chromium, firefox, webkit",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode (visible window)",
    )


@pytest.fixture(scope="session")
def browser_type(request):
    browser_name = request.config.getoption("--browser")
    return browser_name


@pytest.fixture(scope="session")
def headless_mode(request):
    headed = request.config.getoption("--headed")
    return not headed  # If --headed is passed, headless should be False


@pytest.fixture(scope="session")
def browser(browser_type, headless_mode):
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=headless_mode)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=headless_mode)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=headless_mode)
        else:
            raise ValueError(f"Unknown browser: {browser_type}")
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    context.close()
