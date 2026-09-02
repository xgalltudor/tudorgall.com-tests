import pytest
from playwright.sync_api import sync_playwright
from test_resources.pages import Pages


@pytest.fixture(scope="module")
def setup_teardown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        pages = Pages(page)
        pages.open_site()

        yield pages

        browser.close()
