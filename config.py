"""
Application Configuration

Central configuration file for the Network Sniffer.
"""

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "CodeAlpha Basic Network Sniffer"
VERSION = "1.1.0"

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

LOG_LEVEL = "INFO"

# Future use (Lesson 7)
LOG_FILE = "logs/sniffer.log"

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
