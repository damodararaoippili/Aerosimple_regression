import os
import pytest
from utils.browser_setup import setup_browser

@pytest.fixture(scope="function")
def setup():
    headless = False if os.getenv("JENKINS_HOME") is None else True
    driver = setup_browser(browser_name="chrome", headless=headless)
    driver.maximize_window()
    yield driver
    driver.quit()

