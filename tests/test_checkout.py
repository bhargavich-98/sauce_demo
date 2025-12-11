from pages.login_page import LoginPage
from pages.inventory_page import *
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_end_to_end_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = CheckoutOverviewPage(driver)
    complete = CheckoutCompletePage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    login.wait_for_inventory_page()
    assert inventory.is_loaded()

    #Close popup through inventory page object
    inventory = InventoryPage(driver)
    inventory.close_data_breach_popup()
    assert len(inventory.get_all_products()) > 0, "Products list is empty, potential login/session failure."

    inventory.add_first_item_to_cart()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(InventoryPage._badge, '1'))
    inventory.open_cart()
    time.sleep(2)  # Give page time to load
    
    items = cart.get_items()
    print("Cart items found:", len(items))
    assert len(items) > 0, "No items found in cart"

    cart.click_checkout()
    checkout.fill_information("Ammu", "QA", "500001")
    checkout.click_continue()

    overview.click_finish()

    assert complete.is_success(), "Checkout did not complete successfully"