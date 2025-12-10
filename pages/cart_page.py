from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    _items = (By.CLASS_NAME, "cart_item")
    _checkout_btn = (By.ID, "checkout")

    def get_items(self):
        return self.driver.find_elements(*self._items)

    def click_checkout(self):
        self.click(*self._checkout_btn)
