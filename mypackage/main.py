"""
The main module
"""
import logging

logger = logging.getLogger("mypackage")


def do_something():
    """
    Prints 'Doing something'
    """
    logger.debug("Doing something")


def do_something_else():
    """
    Prints 'Doing something else'
    """
    logger.debug("Doing something else")
