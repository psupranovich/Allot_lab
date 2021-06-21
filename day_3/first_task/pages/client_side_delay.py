from time import sleep

from .base_page import BasePage
from day_3.first_task.locators import MainPageLocators, ClientSideDelayLocators


class ClientSideDelay(BasePage):
    def go_to_client_side_page(self):
        login_link = self.browser.find_element(*MainPageLocators.CLIENT_SIDE_DELAY)
        login_link.click()
        return ClientSideDelay(browser=self.browser, url=self.browser.current_url)

        # self.browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

    def should_be_client_side_page(self):
        button = self.browser.find_element(*ClientSideDelayLocators.BUTTON)
        # self.browser.implicitly_wait(5) - не рботает?
        sleep(3) #TODO
        button.click()
        return ClientSideDelay(browser=self.browser, url=self.browser.current_url)


    def client_side_page_element_appear(self):
        self.browser.find_element(*ClientSideDelayLocators.CLIENT_LOADED_DATA)
        assert self.is_element_present(*ClientSideDelayLocators.CLIENT_LOADED_DATA), \
            "Data is not appeared"

