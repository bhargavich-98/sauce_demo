from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    _header = (By.CLASS_NAME, "complete-header")

    def is_success(self):
        return self.find(*self._header).text == "Thank you for your order!"
