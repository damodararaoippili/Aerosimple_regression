import time

import pytest

from pages.Workorders.AWO.send_back_to_maintenance import AWO_send_back_maintenance
from tests.conftest import setup
from tests.test_login import test_login
from utils.module_data_reader import get_testcase_data
@pytest.mark.smoke
def test_send_back_maintenance(test_login):
    wo_send_back_to_maintenace = AWO_send_back_maintenance(test_login)
    testdata = get_testcase_data('AWO', "TC_AW003")
    input_time = testdata.get('Input_time')
    Description_of_work_done = testdata.get('Description of work done')
    wo_send_back_to_maintenace.click_Apps()
    wo_send_back_to_maintenace.Module('Work Orders')
    wo_send_back_to_maintenace.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    wo_send_back_to_maintenace.verify_work_order_status()
    time.sleep(3)