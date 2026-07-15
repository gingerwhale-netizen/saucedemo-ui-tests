from playwright.sync_api import expect
from ui.pages.catalog_page import CatalogPage
from ui.steps.catalog_steps import CatalogSteps

def test_count_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    assert steps.get_products_count() == 6


def test_sorted_by_name(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.sort_items("az")
    names = steps.get_product_names()
    assert names == sorted(names), "Товары не отсортированы по имени A-Z"


def test_sort_by_name_z_to_a(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.sort_items("za")
    names = steps.get_product_names()
    assert names == sorted(names, reverse=True), "Товары не отсортированы по имени Z-A"


def test_sort_by_price(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.sort_items("lohi")
    prices = steps.get_product_prices()
    assert prices == sorted(prices),"Товары не отсортированы по цене low → high"

    steps.sort_items("hilo")
    prices = steps.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Товары не отсортированы по цене high → low"



def test_add_to_cart(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.add_to_cart("Sauce Labs Bike Light")
    assert steps.get_cart_count() == 1


def test_add_sauce_labs_onesie_to_cart(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.add_to_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 1

    steps.remove_from_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 0


def test_product_details_onesie(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Onesie")

    assert detail_name == name, "Название товара не совпадает"
    assert detail_price == price, "Цена товара не совпадает"


def test_product_details_fleece_jacket(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Fleece Jacket")

    assert detail_name == name, "Название товара не совпадает"
    assert detail_price == price, "Цена товара не совпадает"


def test_remove_item_from_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.add_to_cart("Test.allTheThings() T-Shirt (Red)")
    assert steps.get_cart_count() == 1
    steps.remove_from_cart("Test.allTheThings() T-Shirt (Red)")
    assert steps.get_cart_count() == 0


def test_remove_onesie_from_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    steps.add_to_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 1
    steps.remove_from_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 0
