"""
Basic Integration Tests

Tests the interaction between multiple modules.
"""

import os

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

from modules.exporter import (
    initialize_exports,
    export_csv,
    export_json,
    export_pcap,
)

from modules.statistics import (
    initialize_statistics,
    update_statistics,
    finish_statistics,
    stats,
)


# ==========================================================
# Export Workflow
# ==========================================================

def test_export_workflow():
    """
    Verify CSV and JSON export workflow.
    """

    initialize_exports()

    export_csv(
        packet_number=1,
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        length=100,
    )

    export_json(
        packet_number=1,
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        length=100,
    )

    assert os.path.exists("exports/packets.csv")
    assert os.path.exists("exports/packets.json")


# ==========================================================
# Statistics Workflow
# ==========================================================

def test_statistics_workflow():
    """
    Verify statistics workflow.
    """

    initialize_statistics()

    update_statistics(
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        packet_size=120,
    )

    finish_statistics()

    assert stats["total"] == 1
    assert stats["tcp"] == 1
    assert stats["packet_sizes"] == [120]
    assert stats["end_time"] is not None


# ==========================================================
# PCAP Export
# ==========================================================

def test_pcap_export():
    """
    Verify PCAP export.
    """

    initialize_exports()

    packet = Ether() / IP()

    export_pcap(packet)

    assert os.path.exists("exports/capture.pcap")


# ==========================================================
# End-to-End Workflow
# ==========================================================

def test_end_to_end():
    """
    Verify complete export workflow.
    """

    initialize_exports()
    initialize_statistics()

    packet = Ether() / IP()

    export_csv(
        packet_number=1,
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        length=len(packet),
    )

    export_json(
        packet_number=1,
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        length=len(packet),
    )

    export_pcap(packet)

    update_statistics(
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        packet_size=len(packet),
    )

    finish_statistics()

    assert os.path.exists("exports/packets.csv")
    assert os.path.exists("exports/packets.json")
    assert os.path.exists("exports/capture.pcap")

    assert stats["total"] == 1
    assert stats["tcp"] == 1
