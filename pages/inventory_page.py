from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time

class InventoryPage(BasePage):
    _page_title = (By.CLASS_NAME, "title")
    _add_first = (By.XPATH, "(//button[contains(@data-test,'add-to-cart')])[1]")
    _cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    _items = (By.CLASS_NAME, "inventory_item")
    _badge = (By.CLASS_NAME, "shopping_cart_badge")
    _popup_close_btn = (By.CSS_SELECTOR, "button.error-button")

    def is_loaded(self):
        return self.find(*self._page_title).text.strip() == "Products"

    def close_data_breach_popup(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self._popup_close_btn)
            ).click()
            print("Popup closed successfully")
        except TimeoutException:
            print("No popup appeared, continuing...")
        except Exception as e:
            print(f"Error closing popup: {e}")

    def add_first_item_to_cart(self):
        self.close_data_breach_popup()  # handle popup first

        try:
            btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self._add_first)
            )
            btn.click()
        except TimeoutException:
            print("Add to Cart button not clickable!")
            raise
        except Exception:
            # fallback click via JS
            btn = self.driver.find_element(*self._add_first)
            self.driver.execute_script("arguments[0].click();", btn)

    def open_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._cart_icon)
        ).click()

    def get_all_products(self):
        return self.driver.find_elements(*self._items)

    def get_cart_count(self):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(*self._badge))
            return element.text
        except:
            return "0"
