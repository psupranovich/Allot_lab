from first_task.locators import MainPageLocators, ClickLocators
from .base_page import BasePage


class BadClick(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.CLICK)

    def press_the_button_on_the_page(self):
        self.click_element(ClickLocators.BUTTON_CLICK)

    def new_button_color(self):
        return self.find_element(ClickLocators.BUTTON_CLICK_GREEN)






