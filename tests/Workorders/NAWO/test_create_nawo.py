import time
from pages.Workorders.NAWO.create_workorder import CreateNAWO
from utils.module_data_reader import get_testcase_data
from tests.conftest import setup
from tests.test_login import test_login
def test_create_work_order(test_login):
    create_nawo = CreateNAWO(test_login)
    testdata = get_testcase_data('NAWO',"TC_NAW001")
    priority = testdata.get('Priority')
    category = testdata.get('Category')
    description = testdata.get('Problem Description')

    time.sleep(5)
    create_nawo.click_Apps()
    create_nawo.Module('Work Orders')
    create_nawo.Sub_Module('Non-Airfield Work Orders')
    time.sleep(10)
    create_nawo.New_Work_Order()
    create_nawo.Priority(priority)
    create_nawo.Category(category)
    create_nawo.Description(description)
    create_nawo.Create()
    time.sleep(10)