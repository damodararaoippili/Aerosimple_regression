from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def setup_browser(browser_name="chrome", headless=False):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    return driver
