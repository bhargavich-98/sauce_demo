from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time
import pytest

def test_inventory_page_load(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(5)
    assert inventory.is_loaded()
    time.sleep(5)
    assert len(inventory.get_all_products()) > 0

def test_add_first_item_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(5)
    
    inventory.add_first_item_to_cart()
    time.sleep(5)

    assert inventory.get_cart_count() == 1
    print("\n", inventory.get_cart_count())


def test_open_cart_page(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(5)
    inventory.open_cart()
    time.sleep(5)
    assert "cart" in driver.current_url
    print(driver.current_url)