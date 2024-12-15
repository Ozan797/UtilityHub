import argparse
from cli import monitor
import time
import os
from tqdm import tqdm
from colorama import init, Fore, Style


init(autoreset=True)

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
    
    monitor_parser.add_argument(
        "--all",
        action="store_true",
        help="Display full system usage"
    )
    
    monitor_parser.add_argument(
        "--sleep",
        type=int,
        help="Update stats every N second"
    )
    
    monitor_parser.add_argument(
        "--log", 
        action="store_true", 
        help="Save stats to a log file"
    )

    
    monitor_parser.set_defaults(func=run_monitor)

    args = parser.parse_args()

    if hasattr(args, "func"):  # Check if a command was provided
        args.func(args)  # Call the function linked to the command
    else:
        parser.print_help()  # Show help if no command is provided


# Function to Handle the 'monitor' Command
def run_monitor(args):
    while True:
        # Clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.MAGENTA + Style.BRIGHT + "=== System Resource Monitor ===\n")
        
        # Display stats
        if args.all:
            monitor.get_cpu_usage(log=args.log)
            monitor.get_memory_usage(log=args.log)
            monitor.get_disk_usage(log=args.log)
        else:
            if args.cpu:
                monitor.get_cpu_usage(log=args.log)
            if args.memory:
                monitor.get_memory_usage(log=args.log)
            if args.disk:
                monitor.get_disk_usage(log=args.log)

        # If no flags provided
        if not (args.cpu or args.memory or args.disk or args.all):
            print("No flags provided. Use --cpu, --memory, --disk, or --all to display resource usage.")
            break

        # Progress bar for sleep
        if args.sleep:
            print("\n" + Fore.CYAN + Style.BRIGHT + "Refreshing stats... 🌟")
            for i in tqdm(range(args.sleep), 
                          desc="⏳ Please wait", 
                          bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} seconds", 
                          ascii="▒█", 
                          ncols=60):
                time.sleep(1)
        else:
            break
        
# Entry Point of the Script
if __name__ == "__main__":
    main()