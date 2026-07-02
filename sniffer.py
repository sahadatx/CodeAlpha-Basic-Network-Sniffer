"""
Main Entry Point
"""

from config import APP_NAME, HEADER_DIVIDER, VERSION
from modules.capture import start_capture


def main():
    """
    Start the Network Sniffer.
    """

    print(HEADER_DIVIDER)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(HEADER_DIVIDER)

    start_capture()


if __name__ == "__main__":
    main()
