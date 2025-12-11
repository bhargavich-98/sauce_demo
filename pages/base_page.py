from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url="https://www.saucedemo.com"):
        self.driver = driver
        self.base_url = base_url

    def go_to(self, path="/"):
        self.driver.get(self.base_url + path)

    def find(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    def close_data_breach_popup_if_visible(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='error-button']"))
            ).click()
        except:
            pass

    def click(self, by, value, timeout=10):
        self.find(by, value, timeout).click()

    def type(self, by, value, text, timeout=10):
        el = self.find(by, value, timeout)
        el.clear()
        el.send_keys(text)