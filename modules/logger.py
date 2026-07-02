"""
Logging Module
"""

import logging
import os

from config import (
    LOG_LEVEL,
    LOG_FILE,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
)


def setup_logger():
    """
    Configure application logger.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("NetworkSniffer")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    # ==========================================
    # File Logger
    # ==========================================

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # ==========================================
    # Console Logger
    # ==========================================

    console_handler = logging.StreamHandler()

    # Only show WARNING and above on console
    console_handler.setLevel(logging.WARNING)

    console_handler.setFormatter(formatter)

    # ==========================================
    # Add Handlers
    # ==========================================

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Global Logger Instance
logger = setup_logger()
