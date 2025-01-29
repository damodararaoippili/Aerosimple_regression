import time
from pages.Workorders.AWO.create_workorder import CreateAWO
from pages.Workorders.AWO.in_progress import In_progress
from pages.Workorders.AWO.work_order_reassignment import work_order_reassignment
from tests.conftest import setup
from tests.test_login import test_login
from utils.module_data_reader import get_testcase_data
def test_work_order_reassignment(test_login):
    awo_reassignment = work_order_reassignment(test_login)
    awo_reassignment.click_Apps()
    awo_reassignment.Module('Work Orders')
    awo_reassignment.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    awo_reassignment.verify_work_order_status_and_click_on_view()
    awo_reassignment.verify_assigned_to_value()
    awo_reassignment.click_on_reassignment()
    awo_reassignment.select_user_or_role("Airport Manager")
    awo_reassignment.email_confirmation("Yes")
    time.sleep(5)
    awo_reassignment.verify_assigned_to_value()
    time.sleep(5)
