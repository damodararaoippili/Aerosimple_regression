import time
import pyautogui
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class CreateNAWO:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "New_work_order": "//span[text()='Create Work Order']/..",
            "Priority": "//select[@name='select-field-priority']",
            "Category": "//select[@name='select-field-category_id']",
            "location_pointer": "//a[@class='leaflet-draw-draw-marker']",
            "pointer_on_map": "//span[text()='Location']/../following-sibling::div",
            "Description": "//span[text()='Problem Description']/../..//textarea",
            "upload_browser": "//span[text()='browse']/..",
            "check box": "//div[@class='fields_field__1V1fp workOrderCreate_halfWidth__2M36v']//span[text()='Check box']/../..//input",
            "Selection": "//div[@class='fields_field__1V1fp workOrderCreate_halfWidth__2M36v']//select",
            "multi_select": "//h3[text()='Multi Column Grid']/../..//div//div//span[text()='Selection']/../..//select",
            "create": "//span[text()='Create']/..",
            "back_to_work_orders": "//span[text()='Back to Airfield Work Orders']/.."
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

    def New_Work_Order(self):
        self.wait_and_click(self.locators['New_work_order'])

    def Priority(self,value):
        priority_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.locators['Priority'])))
        select = Select(priority_element)
        select.select_by_visible_text(value)

    def Category(self,value):
        category_element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Category'])))
        select = Select(category_element)
        select.select_by_visible_text(value)

    def Description(self,value):
        self.wait_and_send_keys(self.locators['Description'],value)

    def Create(self):
        self.wait_and_click(self.locators['create'])