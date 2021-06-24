from first_task.locators import MainPageLocators, InputTextLocators
from .base_page import BasePage


class TextInput(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.TEXT_INPUT)

    def send_key_for_the_button(self):
        return self.send_key('new_one', InputTextLocators.INPUT)

    def press_the_button_on_the_page(self):
        return self.click_element(InputTextLocators.BUTTON)

    def find_updated_button(self):
        return self.find_element(InputTextLocators.UPDATED_BUTTON)
