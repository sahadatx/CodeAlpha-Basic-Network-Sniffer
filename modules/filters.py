"""
Packet Filter Module

Builds Berkeley Packet Filter (BPF) expressions for Scapy.
"""


def build_bpf_filter(filter_type=None, value=None):
    """
    Build a Berkeley Packet Filter (BPF) string.

    Args:
        filter_type (str): Filter type.
        value (str | int): Filter value.

    Returns:
        str | None: BPF filter string.
    """

    if filter_type is None:
        return None

    filter_type = filter_type.lower().strip()

    # ======================================================
    # Protocol Filters
    # ======================================================

    protocol_filters = {
        "tcp": "tcp",
        "udp": "udp",
        "icmp": "icmp",
        "arp": "arp",
    }

    if filter_type in protocol_filters:
        return protocol_filters[filter_type]

    # ======================================================
    # Port Filter
    # ======================================================

    if filter_type == "port":

        if value is None:
            return None

        return f"port {value}"

    # ======================================================
    # Host/IP Filter
    # ======================================================

    if filter_type == "ip":

        if value is None:
            return None

        return f"host {value}"

    # ======================================================
    # Unknown Filter
    # ======================================================

    return None
