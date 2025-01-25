import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.loginpage.login import Login
from utils.login_data_reader import read_logindata
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="function")
def test_login(setup):
    driver = setup
    testdata = read_logindata()
    url = testdata.get("Environment")
    driver.get(url)

    login = Login(driver)
    email = testdata.get("Email")
    password = testdata.get("Password")

    login.enter_email(email)
    login.click_next()
    login.enter_password(password)
    login.click_next()
    return driver
