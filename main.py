from concurrent.futures import ProcessPoolExecutor
from sys import argv

from selenium.common.exceptions import NoSuchElementException

from swipe_bot.bot import TinderBot, BadooBot, OKCBot


def run_bot(site):
    bot_switcher = {"tinder": TinderBot, "okc": OKCBot, "badoo": BadooBot}
    if site.lower() == "tinder":
        # in case the Facebook log in button does not directly appear
        while True:
            try:
                bot = bot_switcher[site.lower()]()
                bot.get_site()
                bot.login()
                break
            except (NoSuchElementException, IndexError):
                bot.driver.close()
                continue
    else:
        # things get simpler with Badoo and OKC
        bot = bot_switcher[site.lower()]()
        bot.get_site()
        bot.login()
    bot.auto_swipe()


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        executor.map(run_bot, argv[1:])
