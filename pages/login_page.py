from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_btn = (By.ID, "login-button")
    _error_message = (By.CSS_SELECTOR, "[data-test='error']")
    _inventory_counter = (By.ID, "inventory_container")
    def open(self):
        self.go_to("/")

    def login(self, username, password):
        self.type(*self._username, username)
        self.type(*self._password, password)
        self.click(*self._login_btn)

    def wait_for_inventory_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self._inventory_counter)
        )

    def get_error(self):
        try:
            return self.find(*self._error_message).text
        except:
            return ""
