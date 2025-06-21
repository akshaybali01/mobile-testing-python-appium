import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

from utilities.logger_util import create_logger


class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.logger=create_logger(self.__class__.__name__)

    def click(self,locator):
        self.logger.info(f"Clicking on {locator}")
        self.driver.find_element(*locator).click()

    def send_keys(self,locator,text):
        self.logger.info(f"Typing {text} into element {locator} ")
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((locator)))

    def click_and_send_keys(self,locator,text):
        self.logger.info("Typing and clicking..")
        element = self.driver.find_element(*locator)
        self.logger.info(f"Clicking on {locator}")
        element.click()
        self.logger.info(f"Typing {text} on element {locator}")
        element.send_keys(text)

    def swipe_up(self):
        self.logger.info("Swiping up..")
        size=self.driver.get_window_size()
        start_x=size['width'] /2
        start_y = size['height']  * .8
        end_y = size['height'] *.2
        self.driver.swipe(start_x,start_y,start_x,end_y,duration=800)
        time.sleep(1)

    def is_displayed(self,locator):
        return self.driver.find_element(*locator).is_displayed()

    def get_text(self,locator):
        text=self.driver.find_element(*locator).text
        self.logger.info(f"Text from {locator}: {text}")
        return text

