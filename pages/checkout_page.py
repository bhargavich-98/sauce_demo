from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    _first = (By.ID, "first-name")
    _last = (By.ID, "last-name")
    _postal = (By.ID, "postal-code")
    _continue = (By.ID, "continue")

    def fill_information(self, first, last, postal):
        self.type(*self._first, first)
        self.type(*self._last, last)
        self.type(*self._postal, postal)

    def click_continue(self):
        self.click(*self._continue)
