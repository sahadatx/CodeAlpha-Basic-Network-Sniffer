"""
Packet Analyzer Module

Extracts useful information from captured packets.
"""

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

from config import (
    SECTION_DIVIDER,
)


def analyze_packet(packet):
    """
    Analyze a captured packet.

    Args:
        packet: Scapy packet object.
    """

    # ==========================
    # Ethernet Layer
    # ==========================

    if packet.haslayer(Ether):
        ether = packet[Ether]

        print("\n[Ethernet Frame]")
        print(SECTION_DIVIDER)
        print(f"Source MAC       : {ether.src}")
        print(f"Destination MAC  : {ether.dst}")

    # ==========================
    # IP Layer
    # ==========================

    if packet.haslayer(IP):
        ip = packet[IP]

        print("\n[IP Header]")
        print(SECTION_DIVIDER)
        print(f"Source IP        : {ip.src}")
        print(f"Destination IP   : {ip.dst}")
        print(f"TTL              : {ip.ttl}")

    # ==========================
    # Packet Information
    # ==========================

    print("\n[Packet Information]")
    print(SECTION_DIVIDER)
    print(f"Packet Length    : {len(packet)} Bytes")
