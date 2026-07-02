"""
Exporter Module

Handles CSV, JSON and PCAP exports.
"""

import csv
import json
import os

from scapy.utils import wrpcap

from config import (
    CSV_EXPORT,
    JSON_EXPORT,
    PCAP_EXPORT,
    EXPORT_DIRECTORY,
    OVERWRITE_EXPORT,
)


# =====================================================
# Initialization
# =====================================================

def initialize_exports():
    """
    Prepare export directory and export files.
    """

    os.makedirs(EXPORT_DIRECTORY, exist_ok=True)

    if OVERWRITE_EXPORT:

        if os.path.exists(CSV_EXPORT):
            os.remove(CSV_EXPORT)

        if os.path.exists(JSON_EXPORT):
            os.remove(JSON_EXPORT)

        if os.path.exists(PCAP_EXPORT):
            os.remove(PCAP_EXPORT)

    initialize_csv()
    initialize_json()


# =====================================================
# CSV Export
# =====================================================

def initialize_csv():
    """
    Create CSV file with column headers.
    """

    if os.path.exists(CSV_EXPORT):
        return

    with open(
        CSV_EXPORT,
        "w",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Packet Number",
            "Protocol",
            "Source IP",
            "Destination IP",
            "Length (Bytes)",
        ])


def export_csv(
    packet_number,
    protocol,
    source_ip,
    destination_ip,
    length,
):
    """
    Export packet information to CSV.
    """

    with open(
        CSV_EXPORT,
        "a",
        newline="",
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            packet_number,
            protocol,
            source_ip,
            destination_ip,
            length,
        ])


# =====================================================
# JSON Export
# =====================================================

def initialize_json():
    """
    Create an empty JSON export file.
    """

    if os.path.exists(JSON_EXPORT):
        return

    with open(
        JSON_EXPORT,
        "w",
    ) as file:

        json.dump([], file, indent=4)


def export_json(
    packet_number,
    protocol,
    source_ip,
    destination_ip,
    length,
):
    """
    Export packet information to JSON.
    """

    packet = {
        "Packet Number": packet_number,
        "Protocol": protocol,
        "Source IP": source_ip,
        "Destination IP": destination_ip,
        "Length (Bytes)": length,
    }

    try:

        with open(
            JSON_EXPORT,
            "r",
        ) as file:

            data = json.load(file)

    except Exception:

        data = []

    data.append(packet)

    with open(
        JSON_EXPORT,
        "w",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
        )


# =====================================================
# PCAP Export
# =====================================================

def export_pcap(packet):
    """
    Append packet to the PCAP file.
    """

    wrpcap(
        PCAP_EXPORT,
        packet,
        append=True,
    )
