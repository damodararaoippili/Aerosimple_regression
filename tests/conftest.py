import pytest
from utils.browser_setup import setup_browser

@pytest.fixture(scope="function")  # This makes the fixture run for each test case
def driver():
    # Setup browser before each test
    driver = setup_browser(browser_name="chrome", headless=False)  # You can also set headless=True here
    yield driver  # Yield the driver to the test
    driver.quit()  # Cleanup and quit the driver after the test
