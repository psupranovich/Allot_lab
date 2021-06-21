from time import sleep

from .base_page import BasePage
from day_3.first_task.locators import AjaxDataLocators, MainPageLocators


class AjaxData(BasePage):
    def go_to_ajax_data_page(self):
        login_link = self.browser.find_element(*MainPageLocators.AJAX_DATA)
        login_link.click()
        return AjaxData(browser=self.browser, url=self.browser.current_url)

        # self.browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

    def should_be_ajax_button_on_ajax_data_page(self):
        button = self.browser.find_element(*AjaxDataLocators.AJAX_BUTTON)
        sleep(5) #TODO
        button.click()

        return AjaxData(browser=self.browser, url=self.browser.current_url)

    def ajax_data_element_appear(self):
        self.browser.find_element(*AjaxDataLocators.LOADED_DATA)
        assert self.is_element_present(*AjaxDataLocators.LOADED_DATA), \
            "Data is not appeared"


