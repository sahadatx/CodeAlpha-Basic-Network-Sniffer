"""
Protocol Detection Module
"""

from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.layers.l2 import ARP, Ether


def detect_protocol(packet):
    """
    Detect protocol information.

    Returns:
        dict
    """

    protocol = {
        "layer2": "Unknown",
        "layer3": "Unknown",
        "transport": "Unknown",
    }

    # Layer 2
    if packet.haslayer(Ether):
        protocol["layer2"] = "Ethernet"

    # Layer 3
    if packet.haslayer(ARP):
        protocol["layer3"] = "ARP"

    elif packet.haslayer(IP):
        protocol["layer3"] = "IPv4"

    # Transport Layer
    if packet.haslayer(TCP):
        protocol["transport"] = "TCP"

    elif packet.haslayer(UDP):
        protocol["transport"] = "UDP"

    elif packet.haslayer(ICMP):
        protocol["transport"] = "ICMP"

    return protocol
