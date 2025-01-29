import time
from pages.Workorders.AWO.create_workorder import CreateAWO
from pages.Workorders.AWO.in_progress import In_progress
from pages.Workorders.AWO.on_hold import On_Hold
from tests.conftest import setup
from tests.test_login import test_login
from utils.module_data_reader import get_testcase_data
def test_in_progress(test_login):
    awo_on_hold = On_Hold(test_login)
    time.sleep(5)
    awo_on_hold.click_Apps()
    awo_on_hold.Module('Work Orders')
    awo_on_hold.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    awo_on_hold.verify_work_order_status_and_click_on_view()
    time.sleep(5)
    awo_on_hold.click_on_update_status()
    time.sleep(5)
    awo_on_hold.click_on_on_hold()
    time.sleep(8)
    awo_on_hold.verify_work_order_on_hold_status_and_click_on_view()
    time.sleep(10)