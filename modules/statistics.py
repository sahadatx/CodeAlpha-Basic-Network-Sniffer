"""
Statistics Module

Maintains live packet statistics.
"""

from collections import Counter
import time

from config import (
    HEADER_DIVIDER,
    SECTION_DIVIDER,
)

# ==========================================================
# Statistics Storage
# ==========================================================

stats = {
    "total": 0,

    "tcp": 0,
    "udp": 0,
    "icmp": 0,
    "arp": 0,
    "unknown": 0,

    "source_ips": Counter(),
    "destination_ips": Counter(),

    "packet_sizes": [],

    "start_time": None,
    "end_time": None,
}


# ==========================================================
# Initialize
# ==========================================================

def initialize_statistics():
    """
    Reset statistics before capture.
    """

    stats["total"] = 0

    stats["tcp"] = 0
    stats["udp"] = 0
    stats["icmp"] = 0
    stats["arp"] = 0
    stats["unknown"] = 0

    stats["source_ips"].clear()
    stats["destination_ips"].clear()

    stats["packet_sizes"].clear()

    stats["start_time"] = time.time()
    stats["end_time"] = None


# ==========================================================
# Update Statistics
# ==========================================================

def update_statistics(
    protocol,
    source_ip,
    destination_ip,
    packet_size,
):
    """
    Update statistics using packet information.
    """

    stats["total"] += 1

    protocol = protocol.upper()

    if protocol == "TCP":
        stats["tcp"] += 1

    elif protocol == "UDP":
        stats["udp"] += 1

    elif protocol == "ICMP":
        stats["icmp"] += 1

    elif protocol == "ARP":
        stats["arp"] += 1

    else:
        stats["unknown"] += 1

    stats["source_ips"][source_ip] += 1
    stats["destination_ips"][destination_ip] += 1

    stats["packet_sizes"].append(packet_size)


# ==========================================================
# Finish Capture
# ==========================================================

def finish_statistics():
    """
    Record capture end time.
    """

    stats["end_time"] = time.time()


# ==========================================================
# Dashboard
# ==========================================================

def print_dashboard():
    """
    Display professional capture statistics dashboard.
    """

    duration = 0.0

    if (
        stats["start_time"] is not None
        and stats["end_time"] is not None
    ):
        duration = (
            stats["end_time"]
            - stats["start_time"]
        )

    packet_sizes = stats["packet_sizes"]

    if packet_sizes:
        minimum = min(packet_sizes)
        maximum = max(packet_sizes)
        average = sum(packet_sizes) / len(packet_sizes)
        total_bytes = sum(packet_sizes)
    else:
        minimum = 0
        maximum = 0
        average = 0
        total_bytes = 0

    total = stats["total"]

    if total > 0:

        tcp_percent = (stats["tcp"] / total) * 100
        udp_percent = (stats["udp"] / total) * 100
        icmp_percent = (stats["icmp"] / total) * 100
        arp_percent = (stats["arp"] / total) * 100
        unknown_percent = (stats["unknown"] / total) * 100

        packet_rate = total / duration
        bytes_per_second = total_bytes / duration

    else:

        tcp_percent = 0
        udp_percent = 0
        icmp_percent = 0
        arp_percent = 0
        unknown_percent = 0

        packet_rate = 0
        bytes_per_second = 0

    top_sources = stats["source_ips"].most_common(5)
    top_destinations = stats["destination_ips"].most_common(5)

    print()
    print(HEADER_DIVIDER)
    print("Capture Statistics Dashboard")
    print(HEADER_DIVIDER)

    print(f"Total Packets        : {total}")
    print(f"Capture Duration     : {duration:.2f} Seconds")
    print(f"Packets / Second     : {packet_rate:.2f}")
    print(f"Bytes / Second       : {bytes_per_second:.2f}")

    print()
    print(SECTION_DIVIDER)
    print("Protocol Distribution")
    print(SECTION_DIVIDER)

    print(f"TCP                  : {stats['tcp']} ({tcp_percent:.1f}%)")
    print(f"UDP                  : {stats['udp']} ({udp_percent:.1f}%)")
    print(f"ICMP                 : {stats['icmp']} ({icmp_percent:.1f}%)")
    print(f"ARP                  : {stats['arp']} ({arp_percent:.1f}%)")
    print(f"Unknown              : {stats['unknown']} ({unknown_percent:.1f}%)")

    print()
    print(SECTION_DIVIDER)
    print("Traffic Summary")
    print(SECTION_DIVIDER)

    print(f"Total Traffic        : {total_bytes} Bytes")
    print(f"Minimum Packet       : {minimum} Bytes")
    print(f"Maximum Packet       : {maximum} Bytes")
    print(f"Average Packet       : {average:.2f} Bytes")

    print()
    print(SECTION_DIVIDER)
    print("Top Source IPs")
    print(SECTION_DIVIDER)

    if top_sources:
        for ip, count in top_sources:
            print(f"{ip:<20} {count:>5} packets")
    else:
        print("-")

    print()
    print(SECTION_DIVIDER)
    print("Top Destination IPs")
    print(SECTION_DIVIDER)

    if top_destinations:
        for ip, count in top_destinations:
            print(f"{ip:<20} {count:>5} packets")
    else:
        print("-")

    print()
    print(HEADER_DIVIDER)
