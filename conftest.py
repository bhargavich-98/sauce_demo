import pytest
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Create reports/screenshots directory if it doesn't exist
reports_dir = "reports"
screenshots_dir = os.path.join(reports_dir, "screenshots")
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Create logs directory inside reports
logs_dir = os.path.join(reports_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Setup logging
log_file = os.path.join(logs_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def driver():
    # Firefox Options for CI
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")   # headless for CI
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")

    # Launch Firefox driver
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    yield driver
    driver.quit()

# Hook to take screenshot and log on any failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_file = os.path.join(screenshots_dir, f"{item.name}_{rep.when}_{timestamp}.png")
            try:
                driver_fixture.save_screenshot(screenshot_file)
                logging.error(f"[{rep.when.upper()}] Test {item.name} failed. Screenshot saved: {screenshot_file}")
            except Exception as e:
                logging.error(f"Failed to take screenshot for {item.name} during {rep.when}: {e}")

        if call.excinfo:
            logging.error(f"Exception in test {item.name} during {rep.when}: {call.excinfo.value}")