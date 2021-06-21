from .base_page import BasePage
from day_3.first_task.locators import MainPageLocators, LoadDelayLocators


class LoadDelay(BasePage):
    def go_to_load_delay_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOAD_DELAY)
        login_link.click()
        return LoadDelay(browser=self.browser, url=self.browser.current_url)

        # self.browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

    def should_be_load_delay_page(self):
        self.browser.find_element(*LoadDelayLocators.BUTTON_APPEARING_AFTER_DELAY).click()
        assert self.is_element_present(*LoadDelayLocators.BUTTON_APPEARING_AFTER_DELAY), \
            "Button is not appeared after delay"
