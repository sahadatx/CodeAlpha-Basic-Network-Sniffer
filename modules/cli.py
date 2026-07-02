"""
Command Line Interface (CLI)

Handles command-line arguments.
"""

import argparse

from config import (
    APP_NAME,
    VERSION,
)


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace
    """

    parser = argparse.ArgumentParser(
        prog="sniffer.py",
        description=APP_NAME,
    )

    # =====================================
    # Packet Capture
    # =====================================

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        help="Number of packets to capture.",
    )

    parser.add_argument(
        "-i",
        "--interface",
        help="Network interface.",
    )

    # =====================================
    # Packet Filters
    # =====================================

    parser.add_argument(
        "-f",
        "--filter",
        choices=[
            "tcp",
            "udp",
            "icmp",
            "arp",
        ],
        help="Protocol filter.",
    )

    parser.add_argument(
        "--port",
        type=int,
        help="Capture packets for a specific port.",
    )

    parser.add_argument(
        "--ip",
        help="Capture packets for a specific IP.",
    )

    # =====================================
    # Version
    # =====================================

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )

    return parser.parse_args()
