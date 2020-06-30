import sys
import traceback
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from secrets import username, password


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)
        sleep(15)

    def btn_click(self, xpath):
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()


class TinderBot(Bot):
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
            sleep(1)
            try:
                # like
                self.btn_click('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            except ElementClickInterceptedException:
                try:
                    # close popup
                    self.btn_click('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                except ElementClickInterceptedException:
                    # close match
                    self.btn_click('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')


class BadooBot(Bot):
    def get_site(self):
        self.driver.get('https://badoo.com')
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
        fb_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                # like
                self.btn_click('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
            except ElementClickInterceptedException:
                try:
                    # close popup
                    self.btn_click('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div')
                except Exception:
                    traceback.print_exc()


if __name__ == '__main__':
    site = sys.argv[1]
    if site.lower() == "tinder":
        # in case the facebook log in button does not directly appear
        while True:
            try:
                bot = TinderBot()
                bot.get_site()
                bot.login()
            except (NoSuchElementException, IndexError):
                bot.driver.close()
                continue
            break
        bot.auto_swipe()
    elif site.lower() == "badoo":
        bot = BadooBot()
        bot.get_site()
        bot.login()
        bot.auto_swipe()
