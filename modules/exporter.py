"""
Exporter Module

Handles packet export functionality.
"""

import csv
import os

from config import CSV_EXPORT


def initialize_csv():
    """
    Create CSV file with header if it does not exist.
    """

    os.makedirs("exports", exist_ok=True)

    if os.path.exists(CSV_EXPORT):
        return

    with open(
        CSV_EXPORT,
        "w",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Packet",
                "Protocol",
                "Source IP",
                "Destination IP",
                "Length",
            ]
        )


def export_csv(
    packet_number,
    protocol,
    source_ip,
    destination_ip,
    length,
):
    """
    Append packet information to CSV.
    """

    with open(
        CSV_EXPORT,
        "a",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                packet_number,
                protocol,
                source_ip,
                destination_ip,
                length,
            ]
        )
