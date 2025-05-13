from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from swipe_bot import BaseBot


class TinderBot(BaseBot):
    def __init__(self):
        super(TinderBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        self.click_button('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')

    def auto_swipe(self):
        self.click_button('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        self.click_button('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        sleep(5)
        while True:
            self._random_delay()
            try:
                self.click_button(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            except ElementClickInterceptedException:
                try:
                    self.click_button('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                    self._logger.debug('Popup closed')
                except NoSuchElementException:
                    try:
                        self.click_button('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                        self._logger.debug("Match closed")
                    except Exception:
                        self._logger.info(f"Total swipe(s) count: {self.swipe_count}")
                        break
            else:
                self.swipe_count += 1
        self.driver.close()


class BadooBot(BaseBot):
    def __init__(self):
        super(BadooBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://badoo.com')
        sleep(2)
        self.click_button('//*[@id="page"]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')

    def auto_swipe(self):
        while True:
            self._random_delay()
            try:
                self.click_button('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
            except ElementClickInterceptedException:
                self.click_button('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div')
                self._logger.debug("Popup closed")
            except Exception:
                self._logger.info(f"Total swipe(s) count: {self.swipe_count}")
                break
            else:
                self.swipe_count += 1
        self.driver.close()


class OKCBot(BaseBot):
    def __init__(self):
        super(OKCBot, self).__init__(__class__.__name__)

    def get_site(self):
        self.driver.get('https://www.okcupid.com')
        sleep(5)

        self.click_button('//*[@id="main_content"]/div/div/div[1]/div[2]/a')
        sleep(2)

        self.click_button('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[3]')

    def auto_swipe(self):
        while True:
            self._random_delay()
            try:
                self.click_button(
                    '//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[2]/div')
            except ElementClickInterceptedException:
                try:
                    self.click_button(
                        '//*[@id="main_content"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button/span')
                    self._logger.debug("Match closed")
                except NoSuchElementException:
                    try:
                        self.click_button('//*[@id="main_content"]/div[4]/div[2]/div/div[1]/div/button[2]')
                        self._logger.debug("Popup closed")
                    except Exception:
                        self._logger.info(f"Total swipe(s) count: {self.swipe_count}")
                        break
            else:
                self.swipe_count += 1
        self.driver.close()
