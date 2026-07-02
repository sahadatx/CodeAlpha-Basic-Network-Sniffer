"""
Unit Tests for CLI Module
"""

from modules.cli import parse_arguments
from unittest.mock import patch


def test_count_argument():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--count",
            "25",
        ],
    ):

        args = parse_arguments()

        assert args.count == 25


def test_filter_argument():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--filter",
            "tcp",
        ],
    ):

        args = parse_arguments()

        assert args.filter == "tcp"


def test_port_argument():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--port",
            "443",
        ],
    ):

        args = parse_arguments()

        assert args.port == 443


def test_ip_argument():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--ip",
            "8.8.8.8",
        ],
    ):

        args = parse_arguments()

        assert args.ip == "8.8.8.8"
