"""
Unit Tests for Packet Filters
"""

from modules.filters import build_bpf_filter


def test_tcp_filter():

    assert build_bpf_filter("tcp") == "tcp"


def test_udp_filter():

    assert build_bpf_filter("udp") == "udp"


def test_icmp_filter():

    assert build_bpf_filter("icmp") == "icmp"


def test_arp_filter():

    assert build_bpf_filter("arp") == "arp"


def test_port_filter():

    assert build_bpf_filter(
        "port",
        443,
    ) == "port 443"


def test_ip_filter():

    assert build_bpf_filter(
        "ip",
        "8.8.8.8",
    ) == "host 8.8.8.8"


def test_invalid_filter():

    assert build_bpf_filter(
        "xyz"
    ) is None
