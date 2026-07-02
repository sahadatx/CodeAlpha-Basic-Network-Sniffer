"""
Protocol Detection Module
"""

from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.layers.l2 import ARP, Ether

from config import COMMON_PORTS


def get_service_name(port):
    """
    Return common service name for a port.
    """
    return COMMON_PORTS.get(port, "Unknown")


def detect_protocol(packet):
    """
    Detect protocol information from a packet.

    Returns:
        dict: Protocol information.
    """

    protocol = {
        "layer2": "Unknown",
        "layer3": "Unknown",
        "transport": "Unknown",
        "src_port": None,
        "dst_port": None,
        "service": "Unknown",
        "flags": "",
        "icmp_type": None,
        "icmp_code": None,
    }

    # ==========================
    # Layer 2
    # ==========================

    if packet.haslayer(Ether):
        protocol["layer2"] = "Ethernet"

    # ==========================
    # Layer 3
    # ==========================

    if packet.haslayer(ARP):
        protocol["layer3"] = "ARP"

    elif packet.haslayer(IP):
        protocol["layer3"] = "IPv4"

    # ==========================
    # TCP
    # ==========================

    if packet.haslayer(TCP):
        tcp = packet[TCP]

        protocol["transport"] = "TCP"
        protocol["src_port"] = tcp.sport
        protocol["dst_port"] = tcp.dport

        # Detect service using destination port first,
        # then source port if needed.
        service = get_service_name(tcp.dport)

        if service == "Unknown":
            service = get_service_name(tcp.sport)

        protocol["service"] = service

        protocol["flags"] = str(tcp.flags)

    # ==========================
    # UDP
    # ==========================

    elif packet.haslayer(UDP):
        udp = packet[UDP]

        protocol["transport"] = "UDP"
        protocol["src_port"] = udp.sport
        protocol["dst_port"] = udp.dport

        service = get_service_name(udp.dport)

        if service == "Unknown":
            service = get_service_name(udp.sport)

        protocol["service"] = service

    # ==========================
    # ICMP
    # ==========================

    elif packet.haslayer(ICMP):
        icmp = packet[ICMP]

        protocol["transport"] = "ICMP"
        protocol["icmp_type"] = icmp.type
        protocol["icmp_code"] = icmp.code

    return protocol
