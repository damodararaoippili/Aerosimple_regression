import time
import pyautogui
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class CreateAWO:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "New_work_order": "//span[text()='New Work Order']/..",
            "Priority": "//select[@name='select-field-priority']",
            "Category": "//select[@name='select-field-category']",
            "Sub category": "//select[@name='select-field-subcategory']",
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

    def Sub_category(self,value):
        sub_category_element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Sub category'])))
        select = Select(sub_category_element)
        select.select_by_visible_text(value)

    def Location_pointer(self):
        self.wait_and_click(self.locators['location_pointer'])

    def Pointer_on_map(self):
        self.wait_and_click(self.locators['pointer_on_map'])

    def Description(self,value):
        self.wait_and_send_keys(self.locators['Description'],value)

    def upload_attachment(self):
        self.wait_and_click(self.locators['upload_browser'])
        time.sleep(2)
        upload_file_attachment = r"C:\Users\damod\OneDrive\Pictures\Screenshots\2022-09-28 (1)"
        pyautogui.write(upload_file_attachment)  # Type the file path in the file dialog
        pyautogui.press('enter')

    def Custom_fields(self,field_name,value):
        custom_field = f"//div[@class='fields_field__1V1fp workOrderCreate_halfWidth__2M36v']//span[text()='{field_name}']/../..//input"
        self.wait_and_send_keys(custom_field,value)

    def Check_box(self):
        self.wait_and_click(self.locators['check box'])

    def Selection(self,value):
        selection_xpath = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['Selection'])))
        selection =Select(selection_xpath)
        selection.select_by_visible_text(value)

    def dynamic_dropdown(self,field_name):
        selection_xpath = f"//span[text()='{field_name}']/../..//div[@class='undefined css-2b097c-container']"
        self.wait_and_click(selection_xpath)

    def section_value(self,value):
        selection_element = f"//div[@class=' css-26l3qy-menu']//div[text()='{value}']"
        self.wait_and_click(selection_element)

    def Global_location(self,field_name):
        global_location = f"//span[text()='{field_name}']/../..//div[@class='fields_multiSelect__wAR8l css-2b097c-container']"
        self.wait_and_click(global_location)

    def Global_location_value(self,value):
        global_value = f"//div[@class=' css-26l3qy-menu']//div[text()='{value}']"
        self.wait_and_click(global_value)

    def Global_custom_fields(self,field_name,value):
        custom_fields = f"//h3[text()='Multi Column Grid']/../..//div//div//span[text()='{field_name}']/..//input"
        self.wait_and_send_keys(custom_fields,value)

    def Date_and_Time(self,field_name):
        date_and_time = f"//span[text()='{field_name}']/../..//div//div[contains(@class,'undefined')]"
        self.wait_and_click(date_and_time)

    def switch_month_to_year(self,field_name):
        month_and_year = f"//span[text()='{field_name}']/../..//th[@class='rdtSwitch']"
        self.wait_and_click(month_and_year)

    def select_month_and_year(self,value):
        month_and_year = f"//td[text()='{value}']"
        self.wait_and_click(month_and_year)

    def select_date(self,field_name,value):
        select_date = f"//span[text()='{field_name}']/../..//tbody//tr//td[contains(@class,'rdtDay') and not(contains(@class,'rdtOld') or contains(@class,'rdtDisabled') or contains(@class,'rdtNew')) and text()='{value}']"
        self.wait_and_click(select_date)

    def multi_select(self,value):
        multi_select = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['multi_select'])))
        select = Select(multi_select)
        select.select_by_visible_text(value)

    def Create(self):
        self.wait_and_click(self.locators['create'])

    def back_to_work_orders(self):
        self.wait_and_click(self.locators['back_to_work_orders'])

    def Last_work_order_id(self):
        all_work_orders = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='general_table__2PiN- general_evenWidth__3o-5r']//tbody//tr//td[1]")))
        work_order_numbers = []
        for work_order in all_work_orders:
            work_order_id = work_order.text.strip()
            if work_order_id.startswith('A-'):
                work_order_number = int(work_order_id[2:])
                work_order_numbers.append(work_order_number)

        if work_order_numbers:
            max_work_order_number = max(work_order_numbers)
            last_work_order_id = f"A-{max_work_order_number}"
            print(f"Recently Created Work Order ID: {last_work_order_id}")
        else:
            print("There is no such recently created work orders id .")




