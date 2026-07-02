"""
Application Banner
"""

from config import (
    APP_NAME,
    VERSION,
    HEADER_DIVIDER,
)


def show_banner():
    """
    Display application banner.
    """

    print(HEADER_DIVIDER)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(HEADER_DIVIDER)
