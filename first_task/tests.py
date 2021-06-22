import unittest
from selenium import webdriver

from first_task.pages.ajax_data import AjaxData
from first_task.pages.click import BadClick
from first_task.pages.client_side_delay import ClientSideDelay
from first_task.pages.load_delay import LoadDelay
from first_task.pages.progress_bar import ProgressBar
from first_task.pages.sample_app import SampleApp
from first_task.pages.scrollbars import Scrollbars

from first_task.pages.text_input import TextInput


class Setup(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()


class TestSampleApp(Setup):

    def test_users_enter_name_and_see_updated_status(self):
        self.page = SampleApp(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.assertEqual(self.driver.title, 'Sample App')
        self.page.input_name()
        self.page.input_password()
        self.page.press_the_button_on_the_page()
        self.page.find_updated_information()
        self.assertTrue(self.page.find_updated_information())

class TestAjaxData(Setup):

    def test_user_can_see_data_on_ajax_page(self):
        self.page = AjaxData(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.page.press_the_button_on_the_page()
        self.assertEqual(self.driver.title, 'AJAX Data')
        self.page.find_element_with_data()
        self.assertTrue(self.page.find_element_with_data())


class TestProgressBar(Setup):

    def test_user_see_75_on_the_proggress_bar(self):
        self.page = ProgressBar(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.page.press_the_start_button_on_the_page()
        self.assertEqual(self.driver.title, 'Progress Bar')
        self.page.find_value_and_stop()
        self.assertTrue(self.page.bar_result())


class TestLoadDealay(Setup):

    def test_user_can_load_delay_page(self):
        self.page = LoadDelay(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.page.press_the_button_on_the_page()
        self.assertEqual(self.driver.title, 'Load Delays')


class TestClientSideDelay(Setup):

    def test_user_can_see_page_element(self):
        self.page = ClientSideDelay(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.assertEqual(self.driver.title, 'Client Side Delay')
        self.page.press_the_button_on_the_page()
        self.page.client_side_page_element_appeared()
        self.assertTrue(self.page.client_side_page_element_appeared())

#
class TestBadClick(Setup):

    def test_uset_can_cLick_on_bad_button(self):
        self.page = BadClick(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.assertEqual(self.driver.title, 'Click')
        self.page.press_the_button_on_the_page()
        self.page.new_button_color()
        self.assertTrue(self.page.new_button_color())


class TestTextInput(Setup):

    def test_user_can_see_updated_button(self):
        self.page = TextInput(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.assertEqual(self.driver.title, 'Text Input')
        self.page.send_key_for_the_button()
        self.page.press_the_button_on_the_page()
        self.page.find_updated_button()
        self.assertTrue(self.page.find_updated_button())


#
# class TestScrollbars(Setup):
#
#     def test_the_user_can_scroll_and_press_the_button(self):
#         self.page = Scrollbars(self.driver)
#         self.page.go_to_site()
#         self.page.open_page_button()
#         self.assertEqual(self.driver.title, 'Scrollbars')
#         self.page.find_the_button_on_the_page()
#         # self.page.click_element()
#         # self.assertTrue(self.page.click_element)
    #TODO script problem


if __name__ == '__main__':
    from multiprocessing import Process
    procs = []
    procs.append(Process(target=unittest.main, kwargs={'verbosity': 2}))
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

