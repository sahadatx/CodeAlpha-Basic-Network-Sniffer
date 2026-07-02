"""
Packet Capture Module

Handles live packet capturing using Scapy.
"""

from scapy.all import sniff


def packet_callback(packet):
    """
    Called for every captured packet.
    """

    print(packet.summary())


def start_capture(interface=None, count=10):
    """
    Start live packet capture.

    Args:
        interface (str): Network interface.
        count (int): Number of packets to capture.
    """

    print("=" * 50)
    print("Starting Packet Capture...")
    print("=" * 50)

    sniff(
        iface=interface,
        prn=packet_callback,
        count=count,
        store=False
    )

    print("\nCapture Completed.")
