import logging
import os
from logging.handlers import TimedRotatingFileHandler

import coloredlogs

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def get_file_handler(file_name):
    os.makedirs("logs", exist_ok=True)
    file_handler = TimedRotatingFileHandler(os.path.join("logs", f"{file_name}.log"), when="midnight")
    file_handler.setFormatter(logging.Formatter(FORMAT))
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    coloredlogs.install(level="DEBUG", logger=logger, milliseconds=True,
                        fmt=FORMAT)
    logger.addHandler(get_file_handler(logger_name))
    # logger.propagate = False
    return logger
