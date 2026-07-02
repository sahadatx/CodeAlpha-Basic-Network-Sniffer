"""
Main Entry Point
"""

from modules.banner import show_banner
from modules.capture import start_capture
from modules.cli import parse_arguments


def main():
    """
    Start the Network Sniffer.
    """

    show_banner()

    args = parse_arguments()

    filter_type = None
    filter_value = None

    # ==========================================
    # Protocol Filter
    # ==========================================

    if args.filter:

        filter_type = args.filter

    # ==========================================
    # Port Filter
    # ==========================================

    elif args.port:

        filter_type = "port"
        filter_value = args.port

    # ==========================================
    # IP Filter
    # ==========================================

    elif args.ip:

        filter_type = "ip"
        filter_value = args.ip

    start_capture(
        interface=args.interface,
        count=args.count,
        filter_type=filter_type,
        filter_value=filter_value,
    )


if __name__ == "__main__":
    main()
