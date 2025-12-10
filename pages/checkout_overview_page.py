from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    _finish = (By.ID, "finish")

    def click_finish(self):
        self.click(*self._finish)
