import logging
import os
from logging.handlers import TimedRotatingFileHandler

import coloredlogs

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_file_handler(file_name):
    os.makedirs(os.path.join(ROOT_DIR, "logs"), exist_ok=True)
    file_handler = TimedRotatingFileHandler(os.path.join(ROOT_DIR, "logs", f"{file_name}.log"), when="midnight")
    file_handler.setFormatter(logging.Formatter(FORMAT))
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(level="DEBUG", logger=logger, milliseconds=True, fmt=FORMAT)
    logger.addHandler(get_file_handler(logger_name))
    logger.propagate = False
    return logger
