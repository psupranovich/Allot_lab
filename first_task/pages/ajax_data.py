from .base_page import BasePage
from first_task.locators import AjaxDataLocators, MainPageLocators


class AjaxData(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.AJAX_DATA)

    def press_the_button_on_the_page(self):
        self.click_element(AjaxDataLocators.AJAX_BUTTON)

    def find_element_with_data(self):
        return self.find_element(AjaxDataLocators.LOADED_DATA)
