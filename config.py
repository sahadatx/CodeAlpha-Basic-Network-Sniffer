"""
Application Configuration

Central configuration file for the Network Sniffer.
"""

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "CodeAlpha Basic Network Sniffer"
VERSION = "1.2.0"

# ==========================================================
# Packet Capture Configuration
# ==========================================================

# Default network interface.
# None = Automatically select the default interface.
DEFAULT_INTERFACE = None

# Number of packets to capture.
CAPTURE_COUNT = 10

# Store packets in memory.
# (False saves memory)
STORE_PACKETS = False

# ==========================================================
# Logging Configuration
# ==========================================================

# Available Levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

LOG_LEVEL = "INFO"

LOG_FILE = "logs/sniffer.log"

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(message)s"

LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# ==========================================================
# Output Formatting
# ==========================================================

HEADER_DIVIDER = "=" * 60
SECTION_DIVIDER = "-" * 60

# ==========================================================
# Common Network Services
# ==========================================================

COMMON_PORTS = {

    # FTP
    20: "FTP-DATA",
    21: "FTP",

    # Remote Access
    22: "SSH",
    23: "TELNET",

    # Email
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",

    # Network Services
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    123: "NTP",
    161: "SNMP",

    # Directory Services
    389: "LDAP",
    636: "LDAPS",

    # Web
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate",

    # Database
    1433: "Microsoft SQL Server",
    3306: "MySQL",
    5432: "PostgreSQL",

    # Remote Desktop
    3389: "Remote Desktop (RDP)",
    5900: "VNC",

    # Google Services
    5228: "Google Play Services",
}

# ==========================================================
# Packet Filter Configuration
# ==========================================================

# Examples:
#
# FILTER_TYPE = None
#
# FILTER_TYPE = "tcp"
#
# FILTER_TYPE = "udp"
#
# FILTER_TYPE = "icmp"
#
# FILTER_TYPE = "arp"
#
# FILTER_TYPE = "port"
# FILTER_VALUE = 443
#
# FILTER_TYPE = "ip"
# FILTER_VALUE = "8.8.8.8"

FILTER_TYPE = None
FILTER_VALUE = None


# ==========================================================
# Export Configuration
# ==========================================================

# Export directory
EXPORT_DIRECTORY = "exports"

# CSV Export
CSV_EXPORT = f"{EXPORT_DIRECTORY}/packets.csv"

# JSON Export
JSON_EXPORT = f"{EXPORT_DIRECTORY}/packets.json"

# PCAP Export
PCAP_EXPORT = f"{EXPORT_DIRECTORY}/capture.pcap"

# ==========================================================
# Export Behavior
# ==========================================================

# True  -> Create new export files on every run
# False -> Append to existing export files
OVERWRITE_EXPORT = True
