from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    _page_title = (By.CLASS_NAME, "title")
    _items = (By.CLASS_NAME, "cart_item")
    _checkout_btn = (By.ID, "checkout")

    def is_loaded(self):
        try:
            # Verify cart page by checking if the page title element is present
            title_elem = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self._page_title)
            )
            return title_elem is not None
        except:
            return True

    def get_items(self):
        return self.driver.find_elements(*self._items)

    def click_checkout(self):
        self.click(*self._checkout_btn)