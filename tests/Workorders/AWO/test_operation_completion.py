import time
from pages.Workorders.AWO.operation_review import AWO_Operation_review
from tests.conftest import setup
from tests.test_login import test_login
from utils.module_data_reader import get_testcase_data
def test_operation_completion(test_login):
    wo_operation_review = AWO_Operation_review(test_login)
    testdata = get_testcase_data('AWO', "TC_AW004")
    Description_of_work_done = testdata.get('Review Report')
    wo_operation_review.click_Apps()
    wo_operation_review.Module('Work Orders')
    wo_operation_review.Sub_Module('Airfield Work Orders')
    time.sleep(5)
    wo_operation_review.verify_work_order_status()
    time.sleep(3)
    wo_operation_review.review_report(Description_of_work_done)
    wo_operation_review.close_work_order()
    time.sleep(10)