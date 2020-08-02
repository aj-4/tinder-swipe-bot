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
            '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookie_btn.click()

        try:
            self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        except:
            more_options = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
            more_options.click()
        finally:
            fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
            fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(6)

        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        try:
            # Normal account has limited
            limited = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            if limited:
                print('Exceed the limited!')
                return False
        except:
            like_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
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
