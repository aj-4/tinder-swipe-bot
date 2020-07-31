from abc import ABC, abstractmethod
from random import randint
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from logger import get_logger
from secrets import username, password


class BaseBot(ABC):
    def __init__(self, logger_name):
        self.driver = webdriver.Chrome()
        self._logger = get_logger(logger_name)
        self._swipe_count = 0
        self.username = username
        self.password = password

    @abstractmethod
    def get_site(self):
        pass

    @abstractmethod
    def auto_swipe(self):
        pass

    def login(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(self.username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(self.password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)
        self._logger.info("Logged in successfully via Facebook")
        sleep(15)

    def btn_click(self, xpath):
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()


class TinderBot(BaseBot):
    def __init__(self):
        super(TinderBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

    def auto_swipe(self):
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        sleep(5)
        while True:
            sleep(randint(1, 10))
            try:
                self.btn_click('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            except ElementClickInterceptedException:
                try:
                    self.btn_click('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                    self._logger.debug('Popup closed')
                except NoSuchElementException:
                    try:
                        self.btn_click('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                        self._logger.debug("Match closed")
                    except Exception:
                        self._logger.info(f"Total swipe(s) count: {self._swipe_count}")
                        break
            else:
                self._swipe_count += 1


class BadooBot(BaseBot):
    def __init__(self):
        super(BadooBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://badoo.com')
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
        fb_btn.click()

    def auto_swipe(self):
        while True:
            sleep(randint(1, 10))
            try:
                self.btn_click('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
            except ElementClickInterceptedException:
                self.btn_click('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div')
                self._logger.debug("Popup closed")
            except Exception:
                self._logger.info(f"Total swipe(s) count: {self._swipe_count}")
                break
            else:
                self._swipe_count += 1


class OKCBot(BaseBot):
    def __init__(self):
        super(OKCBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://www.okcupid.com')
        sleep(5)

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="main_content"]/div/div/div[1]/div[2]/a')
        sign_in_btn.click()
        sleep(2)

        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[3]')
        fb_btn.click()

    def auto_swipe(self):
        while True:
            sleep(randint(1, 10))
            try:
                self.btn_click('//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[2]/div')
            except ElementClickInterceptedException:
                try:
                    self.btn_click(
                        '//*[@id="main_content"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button/span')
                    self._logger.debug("Match closed")
                except NoSuchElementException:
                    try:
                        self.btn_click('//*[@id="main_content"]/div[4]/div[2]/div/div[1]/div/button[2]')
                        self._logger.debug("Popup closed")
                    except Exception:
                        self._logger.info(f"Total swipe(s) count: {self._swipe_count}")
                        break
            else:
                self._swipe_count += 1
