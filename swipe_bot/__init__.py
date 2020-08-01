import getpass
import os
from abc import ABC, abstractmethod
from random import uniform
from time import sleep

from selenium import webdriver

from logger import get_logger

ID = os.getenv("ID") or input("Enter your Facebook email: ")
PASSWORD = os.getenv("PASSWORD") or getpass.getpass("Enter your Facebook password: ")


class BaseBot(ABC):
    def __init__(self, logger_name):
        self.driver = webdriver.Chrome()
        self._logger = get_logger(logger_name)
        self._swipe_count = 0

    @abstractmethod
    def get_site(self):
        pass

    @abstractmethod
    def auto_swipe(self):
        pass

    def click_button(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def _random_delay(self, min_delay=0, max_delay=10):
        delay = uniform(min_delay, max_delay)
        self._logger.info(f"Sleeping for {delay}s")
        sleep(delay)

    @property
    def swipe_count(self):
        return self._swipe_count

    @swipe_count.setter
    def swipe_count(self, value):
        self._swipe_count = value

    def login(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(ID)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(PASSWORD)

        # click login button
        self.click_button('//*[@id="u_0_0"]')

        self.driver.switch_to.window(base_window)
        self._logger.info("Logged in successfully via Facebook")
        sleep(15)
