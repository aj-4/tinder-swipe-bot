import errno
import os
import random
import signal
import time
from functools import wraps
from typing import Any, Callable, Dict, Tuple

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.remote.webelement import WebElement
from urllib3.exceptions import ProtocolError

import secrets
import session
from matchmaker import MatchMaker


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
    def __init__(self, driver, matchmaker: MatchMaker):
        self.driver = driver
        self.matchmaker = matchmaker

        self.driver.get("https://tinder.com")

    def poll_xpath(self, xpath: str, max_time=5) -> WebElement:
        @timeout(max_time)
        def loop():
            while True:
                try:
                    return self.driver.find_element_by_xpath(xpath)
                except NoSuchElementException:
                    pass
                except Exception:
                    raise
                time.sleep(0.2)

        return loop()

    def login(self) -> None:
        """Login using phone number"""
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

        # Request phone code in prompt
        phone_code = input("Phone verification code: ")

        for idx, ch in enumerate(phone_code):
            num = int(ch)
            code_in = self.poll_xpath(
                f'//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{idx+1}]'
            )
            code_in.send_keys(num)

        code_cont_btn = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button'
        )
        code_cont_btn.click()

        popup_1 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
        )
        popup_1.click()

        popup_2 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
        )
        popup_2.click()

    def like(self) -> None:
        like_btn = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]'
        )
        like_btn.click()

    def super_like(self) -> None:
        super_like_btn = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[2]'
        )
        super_like_btn.click()

    def dislike(self) -> None:
        dislike_btn = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]'
        )
        dislike_btn.click()

    def get_name(self) -> str:
        try:
            name = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span'
            )
        except Exception:
            # Profile has some sort of flair, e.g. college, event
            name = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[1]/div/div/span'
            )
        return name.text

    def get_age(self) -> int:
        try:
            age = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/span'
            )
        except Exception:
            try:
                # Profile has some sort of flair, e.g. college, event
                age = self.poll_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[1]/div/span'
                )
            except Exception:
                # Age field missing
                return -1

        # Age field can exist, but be empty. Returns " " in those cases.
        return int(age.text) if age else -1

    def get_bio(self) -> str:
        try:
            bio_button = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button'
            )
        except Exception:
            # Profile has some sort of flair, e.g. college, event
            bio_button = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/button'
            )

        bio_button.click()

        bio = None

        try:
            bio_field = self.poll_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/span'
            )
            bio = bio_field.text
        except TimeoutError:
            pass
        except ProtocolError:
            # Sometimes the TimeoutError is wrapped in a ProtocolError. Not
            # sure why.
            pass

        close_bio_button = self.poll_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[1]'
        )
        close_bio_button.click()

        return bio

    def close_popup(self) -> None:
        popup_3 = self.poll_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]'
        )
        popup_3.click()

    def close_match(self) -> None:
        match_popup = self.poll_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a'
        )

        try:
            match_popup.click()
        # This will happen on occasion
        except ElementClickInterceptedException:
            time.sleep(5)
            match_popup.click()

    def auto_swipe(self) -> None:
        def try_action(action: Callable[[], Any]):
            try:
                return action()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
                finally:
                    return action()

        while True:
            rand_interval = random.randint(2, 3) + random.random()  # [2, 4]
            time.sleep(rand_interval)

            name = self.get_name()
            age = self.get_age()
            bio = try_action(self.get_bio)

            # Important!
            bio_lower = bio.lower() if bio else None

            super_like, super_reason = self.matchmaker.should_super_like(
                bio_lower
            )
            like, reason = self.matchmaker.should_like(bio_lower)

            swipe_info = {
                "name": name,
                "age": age,
                "bio": bio,
                "like": like,
                "super_like": super_like,
                "reason": super_reason if super_like else reason,
            }
            print(swipe_info)
            self.log_swipe_info(swipe_info)

            if super_like:
                try_action(self.super_like)
            elif like:
                try_action(self.like)
            else:
                try_action(self.dislike)

    def log_swipe_info(self, swipe_info: Dict) -> None:
        log_path = os.path.join(os.getcwd(), "swipes.log")
        with open(log_path, "a") as f:
            f.write(f"{swipe_info}\n")


def prompt_y_n(question) -> bool:
    prompt = f"{question} [Y/n]"
    return input(prompt).lower() != "n"


# =============

chromedriver_path = os.path.join(os.getcwd(), "chromedriver")

matchmaker = MatchMaker()

bot = None
use_last_session = prompt_y_n("Use last session?")

if use_last_session:
    driver = session.connect_existing_webdriver_session(chromedriver_path)
    bot = TinderBot(driver, matchmaker)
else:
    driver = session.open_new_webdriver_session(chromedriver_path)
    bot = TinderBot(driver, matchmaker)
    bot.login()

time.sleep(10)

bot.auto_swipe()
