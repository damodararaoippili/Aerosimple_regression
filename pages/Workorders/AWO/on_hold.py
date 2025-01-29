from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class On_Hold:
    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "resolve": "//span[text()='Resolve']/..",
            "update status": "//span[text()='Update Status']/..",
            "On Hold": "//span[text()='On Hold']/../.."
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

                if "Maintenance Review" in work_order_text or "In Progress" in work_order_text:
                    print(f"Work order found with status: {work_order_text}")
                    try:
                        view_button = work_order.find_element(By.XPATH,".//span[contains(text(), 'Maintenance Review') or contains(text(), 'In Progress')]/../../..//td//a//span[text()='View']/..")
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
                print("No work order with 'Maintenance Review' or 'In Progress' status found.")
        except Exception as e:
            print(f"An error occurred while verifying and clicking on the work order: {e}")

    def click_on_update_status(self):
        try:
            self.wait_and_click(self.locators["update status"])
        except Exception as e:
            print(f"Failed to click on Update Status: {e}")

    def click_on_on_hold(self):
        try:
            self.wait_and_click(self.locators["On Hold"])
        except Exception as e:
            print(f"Failed to click on On Hold: {e}")

    def verify_work_order_on_hold_status_and_click_on_view(self):
        try:
            all_work_orders = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//table[@class='general_table__2PiN- general_evenWidth__3o-5r']//tbody//tr")))

            for work_order in all_work_orders:
                work_order_text = work_order.text.strip()
                print(f"Work Order Text: '{work_order_text}'")

                if "On Hold" in work_order_text:
                    print(f"Work order found with 'On Hold' status: {work_order_text}")

                    try:
                        view_button = work_order.find_element(By.XPATH,".//td//a//span[text()='View']/..")
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
                print("No work order with 'On Hold' status found.")
        except Exception as e:
            print(f"An error occurred while verifying and clicking on the work order: {e}")

