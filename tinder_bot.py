from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import argparse

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, **kwargs):
        self.driver.get('https://tinder.com')

        sleep(2)

        if 'username' in kwargs:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
            fb_btn.click()

            # switch to login popup
            base_window = self.driver.window_handles[0]
            self.driver.switch_to_window(self.driver.window_handles[1])

            email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_in.send_keys(kwargs['username'])

            pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pw_in.send_keys(kwargs['password'])

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()

            self.driver.switch_to_window(base_window)

        elif 'phone' in kwargs:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')))
            phone_button= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
            phone_button.click()
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')))
            phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
            phone_in.send_keys(kwargs['phone'])
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/button')))
            login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            login_btn.click()

            # Wait for user input here
            code = input("Please enter the code sent to your phone: ")

            input_xpath = '//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{}]'
            for i,c in enumerate(code):
                num_in = self.driver.find_element_by_xpath(input_xpath.format(i+1))
                num_in.send_keys(c)
            
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[2]/button')))
            continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            continue_btn.click()
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()



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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--phone', dest='use_phone', action="store_true", default=False)
    args = parser.parse_args()
    
    bot = TinderBot()

    if args.use_phone:
        from secrets import phone
        bot.login(phone=phone)

    else:
        from secrets import username, password
        bot.login(username=username, password=password)
