from time import sleep

from .base_page import BasePage
from day_3.first_task.locators import MainPageLocators, ClientSideDelayLocators


class ClientSideDelay(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.CLIENT_SIDE_DELAY)

    def press_the_button_on_the_page(self):
        return self.click_element(ClientSideDelayLocators.BUTTON)

    def client_side_page_element_appeared(self):
        return self.find_element(ClientSideDelayLocators.CLIENT_LOADED_DATA)


