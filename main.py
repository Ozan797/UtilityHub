import argparse
from cli import monitor

def main():
    parser = argparse.ArgumentParser(
        description="System Management CLI Tool", # Help Description for CLI
        prog="system_monitor" # Program name (Shows in help)
    )
    
    subparser = parser.add_subparsers(
        title="Commands", # Title shown in help
        description="Available Commands",
        help="Use 'system_monitor <command> --help' for more info" # Extra guidance
    )
    
    monitor_parser = subparser.add_parser(
        "monitor", # Name of subcommand
        help="Monitor system resources (CPU, Memory, Disk)"
    )
    
    monitor_parser.add_argument(
        "--cpu",  # Flag name
        action="store_true",  # Makes it a True/False flag
        help="Display CPU usage"  # Help text for this flag
    )
    
    monitor_parser.add_argument(
        "--memory",  # Flag name
        action="store_true",  # Makes it a True/False flag
        help="Display memory usage"  # Help text for this flag
    )
    
    monitor_parser.add_argument(
        "--disk",  # Flag name
        action="store_true",  # Makes it a True/False flag
        help="Display disk usage"  # Help text for this flag
    )
    
    
    monitor_parser.set_defaults(func=run_monitor)

    args = parser.parse_args()

    if hasattr(args, "func"):  # Check if a command was provided
        args.func(args)  # Call the function linked to the command
    else:
        parser.print_help()  # Show help if no command is provided


# Function to Handle the 'monitor' Command
def run_monitor(args):
    if args.cpu:
        monitor.get_cpu_usage()  # Call your CPU function in cli/monitor.py
    if args.memory:
        monitor.get_memory_usage()
    if args.disk:
        monitor.get_disk_usage()
    
    if not (args.cpu or args.memory or args.disk):
        print("No flags provided. Use --help for flag commands")


# Entry Point of the Script
if __name__ == "__main__":
    main()