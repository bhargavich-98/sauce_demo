from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_valid_login(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    assert inventory.is_loaded()

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("invalid", "wrong")
    assert "Epic sadface" in login.get_error()