from first_task.locators import MainPageLocators, LoadDelayLocators
from .base_page import BasePage


class LoadDelay(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.LOAD_DELAY)

    def press_the_button_on_the_page(self):
        self.click_element(LoadDelayLocators.BUTTON_APPEARING_AFTER_DELAY)

