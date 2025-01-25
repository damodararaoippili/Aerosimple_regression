import time

import pytest

from pages.Workorders.AWO.maintenance_review import AWO_Maintenance_review
from utils.module_data_reader import get_testcase_data
from tests.test_login import test_login
from tests.conftest import setup
@pytest.mark.smoke
def test_maintenance_completion(test_login):
    wo_maintenance_review = AWO_Maintenance_review(test_login)
    testdata = get_testcase_data('AWO', "TC_AW003")
    input_time = testdata.get('Input_time')
    Description_of_work_done = testdata.get('Description of work done')
    wo_maintenance_review.click_Apps()
    wo_maintenance_review.Module('Work Orders')
    wo_maintenance_review.Sub_Module('Airfield Work Orders')
    time.sleep(10)
    wo_maintenance_review.verify_work_order_status()
    time.sleep(5)
    wo_maintenance_review.Resolve()
    time.sleep(5)
    wo_maintenance_review.alert_confirmation()
    time.sleep(5)
    wo_maintenance_review.time_tracking(input_time)
    time.sleep(10)
    wo_maintenance_review.Add()
    wo_maintenance_review.Save()
    wo_maintenance_review.description_of_done(Description_of_work_done)
    wo_maintenance_review.Resolve()
    time.sleep(10)