from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.XPATH, "//input[@name='email']")
        self.password_field = (By.XPATH, "//input[@type='password']")
        self.next_button = (By.XPATH, "//button[@type='submit']")
        self.email_validation_text = (By.XPATH, "//span[text()='This field cannot be empty']")
        self.password_validation_text = (By.XPATH, "//span[text()='This field cannot be empty']")


    def enter_email(self, email):
        try:
            email_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.email_field))
            email_element.clear()
            email_element.send_keys(email)
        except StaleElementReferenceException:
            email_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.email_field))
            email_element.clear()
            email_element.send_keys(email)
        except Exception as e:
            raise

    def click_next(self):
        try:
            next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.next_button))
            next_button.click()
        except Exception as e:
            raise

    def enter_password(self, password):
        try:
            password_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field))
            password_element.clear()
            password_element.send_keys(password)
        except Exception as e:
            raise

    def get_email_field_validation(self):
        try:
            email_validation = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.email_validation_text))
            validation_text = email_validation.text
            return validation_text
        except Exception as e:
            return None

    def get_password_field_validation(self):
        try:
            password_validation = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_validation_text))
            validation_text = password_validation.text
            return validation_text
        except Exception as e:
            return None


