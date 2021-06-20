from time import sleep

from .base_page import BasePage
from day_3.locators import  MainPageLocators, ClickLocators


class BadClick(BasePage):
    def go_to_cLick_page(self):
        login_link = self.browser.find_element(*MainPageLocators.CLICK)
        login_link.click()
        return BadClick(browser=self.browser, url=self.browser.current_url)

        # self.browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

    def should_be_cLick_button(self):
        button = self.browser.find_element(*ClickLocators.BUTTON_CLICK)
        # self.browser.implicitly_wait(5) - не рботает?
        sleep(3) #TODO!!!!
        button.click()
        button.click()
        button.click()




