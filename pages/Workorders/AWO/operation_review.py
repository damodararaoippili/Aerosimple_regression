from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AWO_Operation_review:
    def __init__(self,driver):
        self.driver = driver
        self.locators = {
            "Apps": "//div[@class='topbar_menu__3MEY5']",
            "view": "(//span[text()='View']/..)[1]",
            "resolve": "//span[text()='Resolve']/..",
            "input_time": "//div[@class='ui left icon input']//input",
            "add": "//button[@class='back_addTimeBtn__3WBTa']",
            "save": "//button[text()='Save']",
            "description_of_work_order_done": "//textarea[@class='pulpo-textarea undefined']",
            "close_work_order": "//span[text()='Close Work Order']/..",
            "review_report": "//textarea[@class='pulpo-textarea undefined']"

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
        all_work_orders = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='general_table__2PiN- general_evenWidth__3o-5r']//tbody//tr")))
        for work_order in all_work_orders:
            work_order_text = work_order.text.strip()
            if "Operations Review" in work_order_text:
                print("                      ")
                print(f"Found work order: {work_order_text}")
                view_button = work_order.find_element(By.XPATH,".//span[text()='Operations Review']/../../..//td//a//span[text()='View']/..")
                view_button.click()
                break
        else:
            print("No work order with 'Operations Review' status found.")
            return

    def review_report(self,value):
        description = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['review_report'])))
        description.send_keys(value)

    def close_work_order(self):
        close = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.locators['close_work_order'])))
        close.click()
