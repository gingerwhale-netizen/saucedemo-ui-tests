import pytest
from playwright.sync_api import expect

from ui.steps.login_steps import LoginSteps
from ui.steps.catalog_steps import CatalogSteps
from utils.constants import Urls


def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{Urls.BASE}/inventory.html")


def test_login_locked_out_user(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")

    expect(page).to_have_url(f"{Urls.BASE}/")
    assert steps.get_error_text() == "Epic sadface: Sorry, this user has been locked out."


@pytest.mark.parametrize("username", ["standard_user", "visual_user", "error_user"])
def test_logout_parametrized(username, page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login(username, "secret_sauce")
    assert catalog.get_products_count() > 0, "Ожидаем, что в каталоге есть товары"

    catalog.logout()
    expect(page).to_have_url(f"{Urls.BASE}/")
