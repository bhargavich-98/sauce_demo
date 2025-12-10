from pages.login_page import LoginPage
from pages.inventory_page import *
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


def test_end_to_end_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = CheckoutOverviewPage(driver)
    complete = CheckoutCompletePage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_loaded()

    # Close popup through inventory page object
    # inventory = InventoryPage(driver)
    # inventory.close_data_breach_popup()

    inventory.add_first_item_to_cart()
    inventory.open_cart()
    assert int(inventory.get_cart_count()) > 0

    items = cart.get_items()
    print("Cart items found:", items)
    assert len(items) > 0

    cart.click_checkout()
    checkout.fill_information("Ammu", "QA", "500001")
    checkout.click_continue()

    overview.click_finish()

    assert complete.is_success()
