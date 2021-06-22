from .base_page import BasePage
from first_task.locators import MainPageLocators, InputTextLocators, SampleAppLocators


class SampleApp(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.SIMPLE_APP)

    def input_name(self):
        return self.send_key('name', SampleAppLocators.INPUT_NAME)

    def input_password(self):
        return self.send_key('pwd', SampleAppLocators.INPUT_RASSWORD)

    def press_the_button_on_the_page(self):
        return self.click_element(SampleAppLocators.BUTTON)

    def find_updated_information(self):
        name = self.find_element(SampleAppLocators.LOGINSTATUS).text
        if str(name.partition(', ')[2].partition('!')[0]) =='name':
            return True



