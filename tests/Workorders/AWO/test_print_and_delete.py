import time
from pages.Workorders.AWO.create_workorder import CreateAWO
from pages.Workorders.AWO.print_and_delete import print_delete_work_order
from tests.conftest import setup
from tests.test_login import test_login
def test_print_and_delete(test_login):
    awo_print_delete = print_delete_work_order(test_login)
    time.sleep(5)
    awo_print_delete.click_Apps()
    awo_print_delete.Module('Work Orders')
    awo_print_delete.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    awo_print_delete.verify_work_order_status()
    time.sleep(5)
    awo_print_delete.click_on_Actions()
    time.sleep(3)
    awo_print_delete.click_on_Print()
    time.sleep(10)
    awo_print_delete.click_on_Delete()
    time.sleep(5)
    awo_print_delete.Enter_Delete()
    time.sleep(2)
    awo_print_delete.Confirm_Delete()
    time.sleep(10)
