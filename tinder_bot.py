import errno
import os
import signal
import time
from functools import wraps

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.service import Service

import secrets


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


class TinderBot:
    def __init__(self):
        chromedriver_path = os.path.join(os.getcwd(), "chromedriver")
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)

    @timeout(5)
    def poll_xpath(self, xpath: str):
        while True:
            try:
                return self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                pass
            except Exception:
                raise
            time.sleep(0.2)

    def login(self):
        """Login using phone number"""
        self.driver.get("https://tinder.com")

        phone_btn = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button'
        )
        phone_btn.click()

        phone_in = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input'
        )
        phone_in.send_keys(secrets.phone)

        phone_cont_btn = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button'
        )
        phone_cont_btn.click()

        phone_code = input("Phone verification code: ")

        for idx, ch in enumerate(phone_code):
            num = int(ch)
            code_in = self.poll_xpath(
                f'//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{idx+1}]'
            )
            code_in.send_keys(num)

        popup_1 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
        )
        popup_1.click()

        popup_2 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
        )
        popup_2.click()

    def like(self):
        like_btn = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]'
        )
        like_btn.click()

    def dislike(self):
        dislike_btn = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]'
        )
        dislike_btn.click()

    def close_popup(self):
        popup_3 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
        )
        popup_3.click()

    def close_match(self):
        match_popup = self.poll_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'
        )
        match_popup.click()

    def auto_swipe(self):
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


bot = TinderBot()
bot.login()
