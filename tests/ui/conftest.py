import pytest

from utils.constants import Urls


@pytest.fixture
def auth_page(page):
    page.goto(f"{Urls.BASE}/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()
    return page
