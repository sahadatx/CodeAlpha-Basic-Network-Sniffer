"""
Unit Tests for Statistics Module
"""

from modules.statistics import (
    initialize_statistics,
    update_statistics,
    finish_statistics,
    stats,
)


def test_initialize_statistics():
    """
    Verify statistics initialization.
    """

    initialize_statistics()

    assert stats["total"] == 0
    assert stats["tcp"] == 0
    assert stats["udp"] == 0
    assert stats["icmp"] == 0
    assert stats["arp"] == 0
    assert stats["unknown"] == 0
    assert stats["packet_sizes"] == []


def test_update_statistics():
    """
    Verify statistics update.
    """

    initialize_statistics()

    update_statistics(
        protocol="TCP",
        source_ip="192.168.1.10",
        destination_ip="8.8.8.8",
        packet_size=120,
    )

    assert stats["total"] == 1
    assert stats["tcp"] == 1
    assert stats["udp"] == 0
    assert stats["packet_sizes"] == [120]


def test_finish_statistics():
    """
    Verify statistics finish.
    """

    initialize_statistics()

    finish_statistics()

    assert stats["end_time"] is not None
