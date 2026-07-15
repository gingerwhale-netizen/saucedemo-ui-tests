from ui.steps.catalog_steps import CatalogSteps
from ui.steps.basket_steps import BasketSteps
from ui.steps.checkout_steps import CheckoutSteps

def test_add_item_and_check_in_cart(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)

    catalog_steps.add_to_cart("Sauce Labs Backpack")
    basket_steps.open_cart()

    basket_steps.expect_item_in_cart("Sauce Labs Backpack")


def test_add_items_and_check_in_cart(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)

    catalog_steps.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog_steps.add_to_cart("Sauce Labs Fleece Jacket")
    basket_steps.open_cart()

    basket_steps.expect_item_in_cart("Sauce Labs Fleece Jacket")
    basket_steps.expect_item_in_cart("Sauce Labs Bolt T-Shirt")


def test_remove_item_from_cart(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)


    catalog_steps.add_to_cart("Sauce Labs Fleece Jacket")
    basket_steps.open_cart()
    basket_steps.expect_item_in_cart("Sauce Labs Fleece Jacket")
    basket_steps.remove_item("Sauce Labs Fleece Jacket")

    basket_steps.expect_item_not_in_cart("Sauce Labs Fleece Jacket")


def test_remove_items_from_cart(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)


    catalog_steps.add_to_cart("Sauce Labs Backpack")
    catalog_steps.add_to_cart("Test.allTheThings() T-Shirt (Red)")
    basket_steps.open_cart()

    basket_steps.expect_item_in_cart("Sauce Labs Backpack")
    basket_steps.expect_item_in_cart("Test.allTheThings() T-Shirt (Red)")
    basket_steps.remove_item("Sauce Labs Backpack")
    basket_steps.remove_item("Test.allTheThings() T-Shirt (Red)")

    basket_steps.expect_item_not_in_cart("Sauce Labs Backpack")
    basket_steps.expect_item_not_in_cart("Test.allTheThings() T-Shirt (Red)")

def test_checkout_multiple_items(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)


    catalog_steps.add_to_cart("Sauce Labs Fleece Jacket")
    catalog_steps.add_to_cart("Sauce Labs Bolt T-Shirt")
    basket_steps.open_cart()
    basket_total = basket_steps.get_items_total_price()

    checkout_steps = CheckoutSteps(page)
    basket_steps.checkout()
    checkout_steps.start_checkout("Test", "User", "12345")
    assert basket_total == checkout_steps.get_item_total_after_continue()

    checkout_steps.finish_checkout()
    assert checkout_steps.get_success_text() == "Thank you for your order!"

def test_checkout_without_items(page):
    catalog_steps = CatalogSteps(page)
    catalog_steps.login("standard_user", "secret_sauce")
    basket_steps = BasketSteps(page)
    checkout_steps = CheckoutSteps(page)

    catalog_steps.add_to_cart("Sauce Labs Fleece Jacket")
    basket_steps.open_cart()
    basket_steps.checkout()

    checkout_steps.start_checkout("NewUser", "Nrk", "")

    assert checkout_steps.get_error_text() == 'Error: Postal Code is required'