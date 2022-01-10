"""
A utility module
"""

import logging
import logging.config

LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE = "mypackage.log"

logger = logging.getLogger("mypackage")


def do_utility_things() -> None:
    """
    Prints 'Doing utility things'
    """
    logger.debug("Doing utility commands")


def do_more_utility_things() -> None:
    """
    Prints 'Doing more utility things'
    """
    logger.debug("Doing more utility things")


def setup_logging(debug: bool):
    """
    Sets up logging
    """
    logging.config.dictConfig(
        _get_logger_conf(LOGGING_FORMAT, DATE_FORMAT, LOG_FILE, debug)
    )


def _get_logger_conf(
    logging_format: str, date_format: str, log_file: str, debug: bool
) -> dict:
    """
    Returns a logging configuration dictionary
    """

    if debug is True:
        level = "DEBUG"
    else:
        level = "INFO"

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": logging_format, "datefmt": date_format,},
        },
        "handlers": {
            "file": {
                "level": level,
                "class": "logging.FileHandler",
                "filename": log_file,
                "formatter": "standard",
            },
            "console": {
                "level": level,
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
        },
        "loggers": {
            "mypackage": {
                "handlers": ["file", "console"],
                "level": level,
                "propagate": True,
            },
        },
    }
