from .base_page import BasePage
from first_task.locators import MainPageLocators, ProgressBarLocators


class ProgressBar(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.PROGRESS_BAR)

    def press_the_start_button_on_the_page(self):
        return self.click_element(ProgressBarLocators.START_BUTT0N)

    def find_value_and_stop(self):
        self.find_element(ProgressBarLocators.TRUE_VALUE)
        self.click_element(ProgressBarLocators.STOP_BUTTON)

    def bar_result(self):
        result = self.find_element(ProgressBarLocators.RESULT).text
        newresult = int(str(result.partition(': ')[2]).partition(',')[0])
        if -6<=newresult<=6:
            return True



