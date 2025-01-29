from doctest import master
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class work_order_reassignment:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "resolve": "//span[text()='Resolve']/..",
            "reassignment": "//div[@class='back_unassigned__3fa23 ']"
        }

    def wait_and_click(self, xpath, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except ElementClickInterceptedException:
            print(f"Element click intercepted for XPath: {xpath}. Attempting to close modal if present.")
            self.close_modal_if_present()
            try:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            except Exception as e:
                print(f"Failed to click on element after closing modal: {e}")
        except Exception as e:
            print(f"An error occurred while trying to click element with XPath {xpath}: {e}")

    def wait_and_send_keys(self, xpath, value, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(value)
        except ElementClickInterceptedException:
            print(f"Element click intercepted for XPath: {xpath}. Attempting to close modal if present.")
            self.close_modal_if_present()
            try:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).send_keys(
                    value)
            except Exception as e:
                print(f"Failed to send keys to element after closing modal: {e}")
        except Exception as e:
            print(f"An error occurred while trying to send keys to element with XPath {xpath}: {e}")

    def close_modal_if_present(self):
        try:
            modal_close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close')]"))
            )
            modal_close_button.click()
            print("Closed modal successfully.")
        except Exception as e:
            print(f"No modal found or unable to close modal. Error: {e}")

    def click_Apps(self):
        try:
            self.wait_and_click(self.locators['Apps'])
        except Exception as e:
            print(f"Failed to click on Apps: {e}")

    def Module(self, module_name):
        try:
            module_xpath = f"//li//span[text()='{module_name}']/../../../.."
            self.wait_and_click(module_xpath)
        except Exception as e:
            print(f"Failed to click on module {module_name}: {e}")

    def Sub_Module(self, sub_module_name):
        try:
            sub_module_xpath = f"//li//div[@class='d-flex align-items-center']//a//span[text()='{sub_module_name}']/../../.."
            self.wait_and_click(sub_module_xpath)
        except Exception as e:
            print(f"Failed to click on sub-module {sub_module_name}: {e}")

    def verify_work_order_status_and_click_on_view(self):
        try:
            all_work_orders = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//table[@class='general_table__2PiN- general_evenWidth__3o-5r']//tbody//tr")))

            for work_order in all_work_orders:
                work_order_text = work_order.text.strip()
                if "Maintenance Review" in work_order_text:
                    print(f"work order found in 'Maintenance Review': {work_order_text}")
                    try:
                        view_button = work_order.find_element(By.XPATH,
                                                              ".//div[contains(@class, 'workOrderList_maintenance') and contains(., 'Maintenance Review')]//span[text()='Maintenance Review']/../../..//td//a//span[text()='View']/..")
                        view_button.click()
                        break
                    except ElementClickInterceptedException:
                        print(f"Element click intercepted while clicking 'View' for work order: {work_order_text}")
                        self.close_modal_if_present()
                        view_button.click()
                    except Exception as e:
                        print(f"Failed to click on 'View' button for work order: {e}")
                        continue
            else:
                print("No work order with 'Maintenance Review' status found.")
        except Exception as e:
            print(f"An error occurred while verifying and clicking on the work order: {e}")

    def verify_assigned_to_value(self):
        try:
            assigned_to_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH,
                 "//div[@class='workOrderDetail_infoRow__29r3H']//span[text()='Assigned to']/../..//span[@class='workOrderDetail_rowContent__118Qj']/div")))
            assigned_to_text = assigned_to_element.text.strip()

            print(f"Assigned to: '{assigned_to_text}'")
        except Exception as e:
            print(f"An error occurred while extracting the 'Assigned to' value: {e}")

    def click_on_reassignment(self):
        try:
            self.wait_and_click(self.locators['reassignment'])
        except Exception as e:
            print(f"Failed to click on Apps: {e}")

    def select_user_or_role(self, role_or_user_name):
        try:
            user_or_role_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, f"//div[@class='back_userpopup__36ZM2']//ul//li//span[text()='{role_or_user_name}']/..")
            ))
            print(f"Found and selecting: {role_or_user_name}")
            user_or_role_element.click()

        except Exception as e:
            print(f"An error occurred while selecting the role or user: {e}")

    def email_confirmation(self, yes_or_no):
        try:
            email_confirmation = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//span[text()='{yes_or_no}']/.."))
            )
            email_confirmation.click()
        except Exception as e:
            print(f"An error occurred while clicking the email confirmation button: {e}")

