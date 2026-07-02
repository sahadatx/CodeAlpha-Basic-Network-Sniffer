"""
Packet Analyzer Module

Extracts useful information from captured packets.
"""

from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

from config import SECTION_DIVIDER
from modules.protocols import detect_protocol


def analyze_packet(packet):
    """
    Analyze a captured packet.

    Args:
        packet: Scapy packet object.
    """

    # ==========================
    # Protocol Information
    # ==========================

    protocol = detect_protocol(packet)

    print("\n[Protocol Information]")
    print(SECTION_DIVIDER)
    print(f"Layer 2          : {protocol['layer2']}")
    print(f"Layer 3          : {protocol['layer3']}")
    print(f"Protocol         : {protocol['transport']}")

    # ==========================
    # TCP Information
    # ==========================

    if protocol["transport"] == "TCP":

        print("\n[TCP Information]")
        print(SECTION_DIVIDER)
        print(f"Source Port      : {protocol['src_port']}")
        print(f"Destination Port : {protocol['dst_port']}")
        print(f"Service          : {protocol['service']}")
        print(f"Flags            : {protocol['flags']}")

    # ==========================
    # UDP Information
    # ==========================

    elif protocol["transport"] == "UDP":

        print("\n[UDP Information]")
        print(SECTION_DIVIDER)
        print(f"Source Port      : {protocol['src_port']}")
        print(f"Destination Port : {protocol['dst_port']}")
        print(f"Service          : {protocol['service']}")

    # ==========================
    # ICMP Information
    # ==========================

    elif protocol["transport"] == "ICMP":

        print("\n[ICMP Information]")
        print(SECTION_DIVIDER)
        print(f"Type             : {protocol['icmp_type']}")
        print(f"Code             : {protocol['icmp_code']}")

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
