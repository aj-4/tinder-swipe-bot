import os
from collections import namedtuple

from selenium import webdriver


SESSION_FILEPATH = os.path.join(os.getcwd(), "sessioninfo.txt")

Session = namedtuple("Session", "url session_id")


def save_new_session(session: Session) -> None:
    with open(SESSION_FILEPATH, "w") as f:
        f.write(f"{session.url}\n{session.session_id}")


def load_last_session() -> Session:
    with open(SESSION_FILEPATH, "r") as f:
        lines = f.read().split("\n")

    url = lines[0]
    session_id = lines[1]

    return Session(url, session_id)


def connect_existing_webdriver_session(chromedriver_path) -> webdriver.Chrome:
    session = load_last_session()

    driver = webdriver.Remote(
        command_executor=session.url, desired_capabilities={}
    )
    driver.session_id = session.session_id

    return driver


def open_new_webdriver_session(chromedriver_path) -> webdriver.Chrome:
    driver = webdriver.Chrome(executable_path=chromedriver_path)

    session = Session(
        url=driver.command_executor._url, session_id=driver.session_id,
    )
    save_new_session(session)

    return driver
