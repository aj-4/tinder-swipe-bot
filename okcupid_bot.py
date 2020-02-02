from selenium import webdriver
from time import sleep

from secrets import okcupid_username, okcupid_password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.okcupid.com/login')

        cookie_btn = self.driver.find_element_by_xpath('//*[@class="optanon-allow-all accept-cookies-button"]')
        cookie_btn.click()
        sleep(0.5)

        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(okcupid_username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(okcupid_password)
        sleep(0.5)
        try:
            recaptcha_btn = self.driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
            recaptcha_btn.click()
        except Exception:
            sleep(0.5)

        next_btn = self.driver.find_element_by_xpath('//*[@id="OkModal"]/span/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input')
        next_btn.click()

        sleep(1)

        try:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
            fb_btn.click()

            # switch to login popup
            base_window = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[1])
            sleep(2)


            self.driver.switch_to.window(base_window)

            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()

            sleep(2)
            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()

        except Exception:
            sleep(0.5)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
