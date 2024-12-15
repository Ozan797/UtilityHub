from colorama import init, Fore, Style
import psutil
from datetime import datetime

init(autoreset=True)

LOG_FILE = "system_monitor.log"

def log_stats(stat_type, stat_value):
    """Logs stats to a file with a timestamp."""
    with open(LOG_FILE, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {stat_type}: {stat_value}\n")

def print_header(title):
    """Prints a styled header with a border."""
    border = "=" * (len(title) + 4)
    print(Fore.CYAN + Style.BRIGHT + border)
    print(Fore.CYAN + Style.BRIGHT + f"| {title} |")
    print(Fore.CYAN + Style.BRIGHT + border)

def get_cpu_usage(log=False):
    """Displays and optionally logs CPU usage percentage."""
    print_header("CPU USAGE")
    cpu_usage = psutil.cpu_percent()
    print(Fore.YELLOW + f"CPU Usage: {cpu_usage}%\n")
    if log:
        log_stats("CPU Usage", f"{cpu_usage}%")

def get_memory_usage(log=False):
    """Displays and optionally logs memory usage."""
    print_header("MEMORY USAGE")
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)
    used_memory = round(memory.used / (1024 ** 3), 2)
    free_memory = round(memory.available / (1024 ** 3), 2)
    print(Fore.YELLOW + f"Used: {used_memory} GB / Total: {total_memory} GB (Free: {free_memory} GB)\n")
    if log:
        log_stats("Memory Usage", f"Used: {used_memory} GB / Total: {total_memory} GB")

def get_disk_usage(log=False):
    """Displays and optionally logs disk usage."""
    print_header("DISK USAGE")
    disk = psutil.disk_usage('/')
    total_disk = round(disk.total / (1024 ** 3), 2)
    used_disk = round(disk.used / (1024 ** 3), 2)
    free_disk = round(disk.free / (1024 ** 3), 2)
    print(Fore.YELLOW + f"Used: {used_disk} GB / Total: {total_disk} GB (Free: {free_disk} GB)\n")
    if log:
        log_stats("Disk Usage", f"Used: {used_disk} GB / Total: {total_disk} GB")
