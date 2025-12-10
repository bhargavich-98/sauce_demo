from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_btn = (By.ID, "login-button")
    _error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.go_to("/")

    def login(self, username, password):
        self.type(*self._username, username)
        self.type(*self._password, password)
        self.click(*self._login_btn)

    def get_error(self):
        try:
            return self.find(*self._error_message).text
        except:
            return ""
