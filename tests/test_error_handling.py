"""
Error Handling Tests
"""

import pytest
from unittest.mock import patch

from modules.cli import parse_arguments


# ==========================================================
# Invalid Protocol Filter
# ==========================================================

def test_invalid_filter():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--filter",
            "xyz",
        ],
    ):

        with pytest.raises(SystemExit):
            parse_arguments()


# ==========================================================
# Invalid Port
# ==========================================================

def test_invalid_port():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--port",
            "abc",
        ],
    ):

        with pytest.raises(SystemExit):
            parse_arguments()


# ==========================================================
# Missing Port Value
# ==========================================================

def test_missing_port_value():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--port",
        ],
    ):

        with pytest.raises(SystemExit):
            parse_arguments()


# ==========================================================
# Missing IP Value
# ==========================================================

def test_missing_ip_value():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--ip",
        ],
    ):

        with pytest.raises(SystemExit):
            parse_arguments()


# ==========================================================
# Missing Count Value
# ==========================================================

def test_missing_count_value():

    with patch(
        "sys.argv",
        [
            "sniffer.py",
            "--count",
        ],
    ):

        with pytest.raises(SystemExit):
            parse_arguments()
