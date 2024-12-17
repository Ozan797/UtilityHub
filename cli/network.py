import psutil
from colorama import init, Fore, Style

init(autoreset=True)

def show_network_activity():
    """
    Displays network activity (bytes sent and received) using psutil.
    """
    print(Fore.CYAN + Style.BRIGHT + "=== Network Activity ===\n")
    net_io = psutil.net_io_counters()

    sent_mb = net_io.bytes_sent / (1024 * 1024)  # Convert to MB
    recv_mb = net_io.bytes_recv / (1024 * 1024)  # Convert to MB

    print(Fore.YELLOW + f"Data Sent:     {sent_mb:.2f} MB")
    print(Fore.GREEN + f"Data Received: {recv_mb:.2f} MB\n")
