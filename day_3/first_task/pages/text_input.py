from .base_page import BasePage
from day_3.first_task.locators import MainPageLocators, InputTextLocators


class TextInput(BasePage):
    def go_to_text_input_page(self):
        login_link = self.browser.find_element(*MainPageLocators.TEXT_INPUT)
        login_link.click()
        return TextInput(browser=self.browser, url=self.browser.current_url)

        # self.browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

    def user_should_be_able_to_input_text(self):
        self.browser.find_element(*InputTextLocators.INPUTTEXT).send_keys("new_one")
        return TextInput(browser=self.browser, url=self.browser.current_url)

    def user_should_see_new_button_name(self):
        self.browser.find_element(*InputTextLocators.NEW_BUTTON).click()
