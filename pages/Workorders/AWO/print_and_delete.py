from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class print_delete_work_order:
    def __init__(self,driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "Actions":"//span[text()='Actions']/..",
            "Print": "//span[text()='Print']/../..",
            "Delete": "//span[text()='Delete']/../..",
            "Enter_Delete": "//div[@class='delete_confirmDeleteBody__2hJ5H']/input",
            "Confirm_Delete": "//span[text()='Confirm Delete']/.."
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

    def verify_work_order_status(self):
        try:
            # Wait for all work orders to be loaded
            all_work_orders = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//table[@class='general_table__2PiN- general_evenWidth__3o-5r']//tbody//tr")))

            # Loop through all work orders and find one with any status
            for work_order in all_work_orders:
                work_order_text = work_order.text.strip()
                print(f"Work Order Found: {work_order_text}")  # Print the status for debugging
                try:
                    # Find the 'View' button for the current work order
                    view_button = work_order.find_element(By.XPATH, ".//td//a//span[text()='View']/..")

                    # Print details and click on the View button
                    print(f"Clicking 'View' for work order with status: {work_order_text}")
                    view_button.click()
                    break
                except Exception as e:
                    print(f"Error clicking 'View' for work order '{work_order_text}': {e}")

            else:
                print("No work order found with a clickable 'View' button.")
        except Exception as e:
            print(f"An error occurred while verifying work order statuses: {e}")

    def click_on_Actions(self):
        self.wait_and_click(self.locators['Actions'])

    def click_on_Print(self):
        self.wait_and_click(self.locators['Print'])

    def click_on_Delete(self):
        self.wait_and_click(self.locators['Delete'])

    def Enter_Delete(self):
        self.wait_and_send_keys(self.locators['Enter_Delete'],"DELETE")

    def Confirm_Delete(self):
        self.wait_and_click(self.locators['Confirm_Delete'])