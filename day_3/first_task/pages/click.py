from time import sleep

from .base_page import BasePage
from day_3.first_task.locators import  MainPageLocators, ClickLocators


class BadClick(BasePage):

    def go_to_cLick_page(self):
        login_link = self.browser.find_element(*MainPageLocators.CLICK)
        login_link.click()
        return BadClick(browser=self.browser, url=self.browser.current_url)

    def should_be_cLick_button(self):
        button = self.browser.find_element(*ClickLocators.BUTTON_CLICK)
        # self.browser.implicitly_wait(5) - не рботает?
        button.click()






