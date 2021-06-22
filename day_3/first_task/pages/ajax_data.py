from .base_page import BasePage
from day_3.first_task.locators import AjaxDataLocators


class AjaxData(BasePage):

    def click_button_on_ajax_data_page(self):
        button = self.find_button(AjaxDataLocators.AJAX_BUTTON, 5)
        button.click()
        return self.find_element(AjaxDataLocators.LOADED_DATA)

