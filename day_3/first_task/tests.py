import unittest
from asyncio import sleep

from selenium import webdriver
#
# from Allot_lab.day_3.locators import MainPageLocators, LoadDelayLocators
# from first_task.pages.click import BadClick
# from first_task.pages.text_input import TextInput
# from first_task.pages.ajax_data import AjaxData
from day_3.first_task.pages.click import BadClick
from day_3.first_task.pages.client_side_delay import ClientSideDelay
from day_3.first_task.pages.load_delay import LoadDelay

class Setup(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()


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

# def test_user_can_load_ajax_data_and_see_element(browser):
#     resource = 'ajax'
#     ajax_page = AjaxData(browser)
#     ajax_page.go_to_site(resource)
#     new_element = ajax_page.click_button_on_ajax_data_page()
#     assert new_element
#

# def test_user_can_load_cliene_side_data_and_see_element(browser):
#     page = ClientSideDelay(browser, link).open()
#     page.open()
#     client_side_page = page.go_to_client_side_page()
#     new_page = client_side_page.should_be_client_side_page()
#     new_page.client_side_page_element_appear()
#
#
# def test_uset_can_cLick_on_bad_button(browser):
#     page = BadClick(browser, link)
#     page.open()
#     click_page = page.go_to_cLick_page()
#     click_page.should_be_cLick_button()
#
#
# def test_user_can_input_text(browser):
#     page = TextInput(browser, link)
#     page.open()
#     click_on_text_input = page.go_to_text_input_page()
#     new_button_appear = click_on_text_input.user_should_be_able_to_input_text()
#     new_button_appear.user_should_see_new_button_name()
#
#
#
#
#




