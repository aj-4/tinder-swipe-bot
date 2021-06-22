from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from secrets import username, password


class TinderBot():
    def __init__(self):
        options = Options()
        options.add_experimental_option(
            "excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)

        cookie_btn = self.driver.find_element_by_xpath(
            '//*[@id="q-84965404"]/div/div[2]/div/div/div[1]/button')
        cookie_btn.click()

        btn_login = self.driver.find_element_by_xpath(
            '//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        btn_login.click()
        sleep(1)

        try:
            more_options = self.driver.find_element_by_xpath(
                '//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/button')
            if ('Trouble' not in more_options.text):
                more_options.click()
        except:
            sleep(0.1)
        finally:
            fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/div[2]/button')
            fb_btn.click()

        # more_options = self.driver.find_element_by_xpath(
        #     '//*[@id="q-1813346480"]/div/div/div[1]/div/div[3]/span/button')
        # more_options.click()

        # switch to login popup
        sleep(2)
        # return
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0_*"]')
        login_btn = self.driver.find_element_by_xpath(
            '//input[@type="submit"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)

        sleep(6)

        allow_location = self.driver.find_element_by_xpath(
            '//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[1]')
        allow_location.click()

        disable_noti = self.driver.find_element_by_xpath(
            '//*[@id="q-1813346480"]/div/div/div/div/div[3]/button[2]')
        disable_noti.click()

        # popup_1 = self.driver.find_element_by_xpath(
        #     '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_1.click()

        # popup_2 = self.driver.find_element_by_xpath(
        #     '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_2.click()

    def like(self):
        try:
            # print('like')
            # Normal account has limited
            limited = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            if limited:
                print('Exceed the limited!')
                return False
        except:
            like_btn = self.driver.find_element_by_xpath(
                '//*[@id="q-84965404"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
            like_btn.click()
        return True

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        ok = True
        while ok:
            sleep(0.5)
            try:
                ok = self.like()
                if not ok:
                    # Exit app
                    self.driver.quit()
                    exit()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except:
                        self.auto_swipe()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
