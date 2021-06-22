import unittest
from selenium import webdriver
from day_3.first_task.pages.click import BadClick
from day_3.first_task.pages.client_side_delay import ClientSideDelay
from day_3.first_task.pages.load_delay import LoadDelay
from day_3.first_task.pages.text_input import TextInput


class Setup(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

#
# class TestLoadDealay(Setup):
#
#     def test_user_can_load_delay_page(self):
#         self.page = LoadDelay(self.driver)
#         self.page.go_to_site()
#         self.page.open_page_button()
#         self.page.press_the_button_on_the_page()
#         self.assertEqual(self.driver.title, 'Load Delays')
#
#
# class TestClientSideDelay(Setup):
#
#     def test_user_can_see_page_element(self):
#         self.page = ClientSideDelay(self.driver)
#         self.page.go_to_site()
#         self.page.open_page_button()
#         self.assertEqual(self.driver.title, 'Client Side Delay')
#         self.page.press_the_button_on_the_page()
#         self.page.client_side_page_element_appeared()
#         self.assertTrue(self.page.client_side_page_element_appeared())
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






