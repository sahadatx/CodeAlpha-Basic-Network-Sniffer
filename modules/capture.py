"""
Packet Capture Module

Handles live packet capturing using Scapy.
"""

from scapy.all import sniff

from config import (
    CAPTURE_COUNT,
    DEFAULT_INTERFACE,
    HEADER_DIVIDER,
    FILTER_TYPE,
    FILTER_VALUE,
    STORE_PACKETS,
)

from modules.analyzer import analyze_packet
from modules.filters import build_bpf_filter

packet_count = 0


def packet_callback(packet):
    """
    Callback function executed for every captured packet.
    """

    global packet_count

    packet_count += 1

    print(f"\n{HEADER_DIVIDER}")
    print(f"Packet #{packet_count}")
    print(HEADER_DIVIDER)

    analyze_packet(packet)


def start_capture(
    interface=DEFAULT_INTERFACE,
    count=CAPTURE_COUNT,
):
    """
    Start live packet capture.

    Args:
        interface (str): Network interface.
        count (int): Number of packets to capture.
    """

    global packet_count

    packet_count = 0

    print("=" * 50)
    print("Starting Packet Capture...")
    print("=" * 50)

    # Build Berkeley Packet Filter (BPF)
    bpf_filter = build_bpf_filter(
        FILTER_TYPE,
        FILTER_VALUE,
    )

    # Show active filter
    if bpf_filter:
        print(f"BPF Filter : {bpf_filter}")

    sniff(
        iface=interface,
        prn=packet_callback,
        count=count,
        store=STORE_PACKETS,
        filter=bpf_filter,
    )

    print("\nCapture Completed.")
