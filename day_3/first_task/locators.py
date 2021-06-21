from selenium.webdriver.common.by import By


class MainPageLocators():
    LOAD_DELAY = (By.XPATH, "//*[@id='overview']/div/div[1]/div[4]/h3/a")
    AJAX_DATA = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[1]/h3/a')
    CLIENT_SIDE_DELAY = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[2]/h3/a')
    CLICK = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[3]/h3/a')
    TEXT_INPUT = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[4]/h3/a')
    SCROLLBARS = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[1]/h3/a')
    DYNAMIC_TABLE = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[2]/h3/a')
    VERIFY_TEXT = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[3]/h3/a')


class LoadDelayLocators():
    BUTTON_APPEARING_AFTER_DELAY = (By.XPATH,'/html/body/section/div/button')


class AjaxDataLocators():
    LOADED_DATA = (By.CSS_SELECTOR, '#content > p')
    AJAX_BUTTON = (By.CSS_SELECTOR, '#ajaxButton')


class ClientSideDelayLocators():
    CLIENT_LOADED_DATA = (By.XPATH, '/html/body/section/div/div/p')
    BUTTON = (By.XPATH, '/html/body/section/div/button')


class ClickLocators():
    BUTTON_CLICK = (By.CSS_SELECTOR, '#badButton')

class InputTextLocators():
    INPUTTEXT = (By.CSS_SELECTOR, '#newButtonName')
    NEW_BUTTON = (By.CSS_SELECTOR, '#updatingButton')