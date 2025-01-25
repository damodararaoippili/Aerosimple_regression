from argparse import Action
import time
from math import acosh
from selenium.webdriver.support.select import Select
from selenium.common import ElementClickInterceptedException, TimeoutException, ElementNotVisibleException,StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.runtime import ExecutionContextsCleared
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class Edit_AWO:
    def __init__(self,driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "view": "(//span[text()='View']/..)[1]",
            "Actions": "//span[text()='Actions']/..",
            "Edit": "//span[text()='Edit']/../..",
            "Category": "//select[@name='select-field-category']",
            "Sub category": "//select[@name='select-field-subcategory']",
            "Selection": "//div[@class='fields_field__1V1fp workOrderCreate_halfWidth__2M36v']//select",
            "update": "//span[text()='Update']/.."
        }

    def wait_and_click(self, xpath, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except ElementClickInterceptedException:
            self.close_modal_if_present()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    def wait_and_send_keys(self, xpath, value,timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(value)
        except ElementClickInterceptedException:
            self.close_modal_if_present()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(value)

    def close_modal_if_present(self):

        try:
            # Check for a modal and attempt to close it
            modal_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close')]"))
            )
            modal_close_button.click()
            print("Closed modal successfully.")
        except Exception as e:
            print(f"No modal found or unable to close modal. Error: {e}")
            pass  # Ignore if modal is not present or cannot be closed

    def close_modal_if_present(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
        except:
            pass

    def click_Apps(self):
        self.wait_and_click(self.locators['Apps'])

    def Module(self, module_name):
        module_xpath = f"//li//span[text()='{module_name}']/../../../.."
        self.wait_and_click(module_xpath)

    def Sub_Module(self, sub_module_name):
        sub_module_xpath = f"//li//div[@class='d-flex align-items-center']//a//span[text()='{sub_module_name}']/../../.."
        self.wait_and_click(sub_module_xpath)

    def click_on_view(self):
        view = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['view'])))
        actions = ActionChains(self.driver)
        actions.move_to_element(view).click().perform()

    def Click_on_Actions(self):
        Action = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Actions'])))
        actions = ActionChains(self.driver)
        actions.move_to_element(Action).click().perform()
    def Click_on_Edit(self):
        Edit = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Edit'])))
        actions =ActionChains(self.driver)
        actions.move_to_element(Edit).click().perform()

    def Category(self,value):
        category_element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Category'])))
        select = Select(category_element)
        select.select_by_visible_text(value)

    def Sub_category(self,value):
        sub_category_element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Sub category'])))
        select = Select(sub_category_element)
        select.select_by_visible_text(value)

    def Selection(self,value):
        selection_xpath = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Selection'])))
        selection =Select(selection_xpath)
        selection.select_by_visible_text(value)

    def Update(self):
        self.wait_and_click(self.locators['update'])

















