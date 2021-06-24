from first_task.locators import ScrollbarsLocators, MainPageLocators
from .base_page import BasePage


class Scrollbars(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.SCROLLBARS)

    def find_the_button_on_the_page(self):
        element = self.find_element(ScrollbarsLocators.HIDDEN_BUTTON)
        self.driver.executeScript("return arguments[0].scrollIntoView(true);", element)

    def press_to_the_button(self):
        return self.click_element(ScrollbarsLocators.HIDDEN_BUTTON)
