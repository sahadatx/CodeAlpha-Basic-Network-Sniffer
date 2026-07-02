"""
Packet Capture Module

Handles live packet capturing using Scapy.
"""

from scapy.all import sniff
from scapy.layers.inet import IP

from config import (
    CAPTURE_COUNT,
    DEFAULT_INTERFACE,
    FILTER_TYPE,
    FILTER_VALUE,
    HEADER_DIVIDER,
    STORE_PACKETS,
)

from modules.analyzer import analyze_packet
from modules.exporter import (
    initialize_exports,
    export_csv,
    export_json,
    export_pcap,
)
from modules.filters import build_bpf_filter
from modules.logger import logger
from modules.protocols import detect_protocol
from modules.statistics import (
    initialize_statistics,
    update_statistics,
    finish_statistics,
    print_dashboard,
)

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

    # ==================================================
    # Analyze Packet
    # ==================================================

    analyze_packet(packet)

    # ==================================================
    # Prepare Packet Information
    # ==================================================

    protocol = detect_protocol(packet)

    source_ip = "-"
    destination_ip = "-"

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

    # ==================================================
    # Export Packet
    # ==================================================

    try:

        export_csv(
            packet_number=packet_count,
            protocol=protocol["transport"],
            source_ip=source_ip,
            destination_ip=destination_ip,
            length=len(packet),
        )

        export_json(
            packet_number=packet_count,
            protocol=protocol["transport"],
            source_ip=source_ip,
            destination_ip=destination_ip,
            length=len(packet),
        )

        export_pcap(packet)

    except Exception as error:

        logger.error(
            "Export failed: %s",
            error,
        )

    # ==================================================
    # Update Statistics
    # ==================================================

    update_statistics(
        protocol=protocol["transport"],
        source_ip=source_ip,
        destination_ip=destination_ip,
        packet_size=len(packet),
    )


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

    # ==================================================
    # Initialize Modules
    # ==================================================

    initialize_exports()
    initialize_statistics()

    print(HEADER_DIVIDER)
    print("Starting Packet Capture...")
    print(HEADER_DIVIDER)

    # ==================================================
    # Build Berkeley Packet Filter (BPF)
    # ==================================================

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

    # ==================================================
    # Start Packet Capture
    # ==================================================

    try:

        sniff(
            iface=interface,
            prn=packet_callback,
            count=count,
            store=STORE_PACKETS,
            filter=bpf_filter,
        )

        finish_statistics()

        # ==================================================
        # Display Statistics Dashboard
        # ==================================================

        print_dashboard()

        logger.info(
            "Packet capture completed successfully."
        )

    except PermissionError:

        logger.error(
            "Permission denied. Run the program using sudo."
        )

    except KeyboardInterrupt:

        finish_statistics()

        # ==================================================
        # Display Statistics Dashboard
        # ==================================================

        print_dashboard()

        logger.warning(
            "Packet capture stopped by user."
        )

    except Exception as error:

        logger.exception(
            "Unexpected error: %s",
            error,
        )

    print("\nCapture Completed.")
