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
from modules.logger import logger

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

    print(HEADER_DIVIDER)
    print("Starting Packet Capture...")
    print(HEADER_DIVIDER)

    # ==========================================
    # Build Berkeley Packet Filter (BPF)
    # ==========================================

    bpf_filter = build_bpf_filter(
        FILTER_TYPE,
        FILTER_VALUE,
    )

    if bpf_filter:
        print(f"BPF Filter : {bpf_filter}")
        logger.debug(
            "Active BPF Filter: %s",
            bpf_filter,
        )

    # ==========================================
    # Start Packet Capture
    # ==========================================

    try:

        sniff(
            iface=interface,
            prn=packet_callback,
            count=count,
            store=STORE_PACKETS,
            filter=bpf_filter,
        )

        logger.info(
            "Packet capture completed successfully."
        )

    except PermissionError:

        logger.error(
            "Permission denied. Run the program using sudo."
        )

    except KeyboardInterrupt:

        logger.warning(
            "Packet capture stopped by user."
        )

    except Exception as error:

        logger.exception(
            "Unexpected error: %s",
            error,
        )

    print("\nCapture Completed.")
