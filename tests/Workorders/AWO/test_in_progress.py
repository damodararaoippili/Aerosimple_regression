import time
from pages.Workorders.AWO.create_workorder import CreateAWO
from pages.Workorders.AWO.in_progress import In_progress
from tests.conftest import setup
from tests.test_login import test_login
from utils.module_data_reader import get_testcase_data
def test_in_progress(test_login):
    awo_in_progress = In_progress(test_login)
    time.sleep(5)
    awo_in_progress.click_Apps()
    awo_in_progress.Module('Work Orders')
    awo_in_progress.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    awo_in_progress.verify_work_order_status_and_click_on_view()
    time.sleep(5)
    awo_in_progress.click_on_update_status()
    time.sleep(5)
    awo_in_progress.click_on_in_progress()
    time.sleep(8)
    awo_in_progress.verify_work_order_status_and_log_in_progress()
    time.sleep(10)