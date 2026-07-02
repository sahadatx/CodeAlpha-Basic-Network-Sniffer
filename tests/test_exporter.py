"""
Unit Tests for Exporter Module
"""

import os

from modules.exporter import initialize_exports


def test_export_directory_created():
    """
    Verify export directory is created.
    """

    initialize_exports()

    assert os.path.isdir("exports")


def test_csv_file_exists():
    """
    Verify CSV export file is created.
    """

    initialize_exports()

    assert os.path.isfile("exports/packets.csv")


def test_json_file_exists():
    """
    Verify JSON export file is created.
    """

    initialize_exports()

    assert os.path.isfile("exports/packets.json")
