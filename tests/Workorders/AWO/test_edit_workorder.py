import time
from pages.Workorders.AWO.create_workorder import CreateAWO
from tests.conftest import setup
from tests.test_login import test_login
from pages.Workorders.AWO.edit_workorder import Edit_AWO
from utils.module_data_reader import get_testcase_data
def test_edit_work_order(test_login):
    edit_awo = Edit_AWO(test_login)
    testdata = get_testcase_data('AWO',"TC_AW002")
    category = testdata.get('Category')
    sub_category = testdata.get('Sub Category')
    time.sleep(10)
    edit_awo.click_Apps()
    edit_awo.Module('Work Orders')
    edit_awo.Sub_Module('Airfield Work Orders')
    time.sleep(10)
    edit_awo.click_on_view()
    time.sleep(5)
    edit_awo.Click_on_Actions()
    edit_awo.Click_on_Edit()
    edit_awo.Category(category)
    edit_awo.Sub_category(sub_category)
    edit_awo.Update()
    time.sleep(8)

