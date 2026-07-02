"""
Main Entry Point
"""

import sys

from modules.banner import show_banner
from modules.capture import start_capture
from modules.cli import parse_arguments


def main():
    """
    Application entry point.
    """

    # Parse command-line arguments
    args = parse_arguments()

    # Show banner only during normal execution
    if not any(
        arg in sys.argv
        for arg in ("-h", "--help", "-v", "--version")
    ):
        show_banner()

    # Build filter configuration
    filter_type = None
    filter_value = None

    if args.filter:
        filter_type = args.filter

    elif args.port:
        filter_type = "port"
        filter_value = args.port

    elif args.ip:
        filter_type = "ip"
        filter_value = args.ip

    # Start packet capture
    start_capture(
        interface=args.interface,
        count=args.count,
        filter_type=filter_type,
        filter_value=filter_value,
    )


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nInterrupted by user.")

    except Exception as error:
        print(f"\nFatal Error: {error}")
