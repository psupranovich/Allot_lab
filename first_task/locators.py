from selenium.webdriver.common.by import By


class MainPageLocators():
    LOAD_DELAY = (By.XPATH, "//*[@id='overview']/div/div[1]/div[4]/h3/a")
    AJAX_DATA = (By.CSS_SELECTOR, '#overview > div > div:nth-child(2) > div:nth-child(1) > h3 > a')
    CLIENT_SIDE_DELAY = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[2]/h3/a')
    CLICK = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[3]/h3/a')
    TEXT_INPUT = (By.XPATH, '//*[@id="overview"]/div/div[2]/div[4]/h3/a')
    SCROLLBARS = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[1]/h3/a')
    # DYNAMIC_TABLE = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[2]/h3/a')
    # VERIFY_TEXT = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[3]/h3/a')
    PROGRESS_BAR = (By.XPATH, '//*[@id="overview"]/div/div[3]/div[4]/h3/a')
    SIMPLE_APP = (By.XPATH, '//*[@id="overview"]/div/div[4]/div[2]/h3/a')



class LoadDelayLocators():
    BUTTON_APPEARING_AFTER_DELAY = (By.XPATH,'/html/body/section/div/button')


class AjaxDataLocators():
    LOADED_DATA = (By.CSS_SELECTOR, '#content > p')
    AJAX_BUTTON = (By.ID, 'ajaxButton')


class ClientSideDelayLocators():
    CLIENT_LOADED_DATA = (By.XPATH, '/html/body/section/div/div/p')
    BUTTON = (By.XPATH, '/html/body/section/div/button')


class ClickLocators():
    BUTTON_CLICK = (By.CSS_SELECTOR, '[class="btn btn-primary"]')
    BUTTON_CLICK_GREEN = (By.CSS_SELECTOR, '[class = "btn btn-success"]')


class InputTextLocators():
    INPUT = (By.ID, 'newButtonName')
    BUTTON = (By.ID, 'updatingButton')
    UPDATED_BUTTON = (By.XPATH, '//button[contains(.,"new_one")]')


class ProgressBarLocators():
    START_BUTT0N = (By.ID, 'startButton')
    STOP_BUTTON = (By.ID, 'stopButton')
    TRUE_VALUE = (By.CSS_SELECTOR, '[aria-valuenow="75"]')
    RESULT = (By.ID, 'result')


class SampleAppLocators():
    INPUT_NAME = (By.NAME, 'UserName')
    INPUT_RASSWORD = (By.NAME, 'Password')
    BUTTON = (By.ID, 'login')
    LOGINSTATUS = (By.ID, 'loginstatus')


class ScrollbarsLocators():
    HIDDEN_BUTTON = (By.CSS_SELECTOR, '#hidingButton')