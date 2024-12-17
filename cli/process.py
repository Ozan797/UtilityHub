import psutil
from colorama import init, Fore, Style

init(autoreset=True)

def print_header(title):
    """Prints a styled header with borders."""
    border = "=" * (len(title) + 4)
    print(Fore.CYAN + Style.BRIGHT + border)
    print(Fore.CYAN + Style.BRIGHT + f"| {title} |")
    print(Fore.CYAN + Style.BRIGHT + border)

def list_processes(filter_name=None):
    """
    List all active processes with their PID, name, CPU %, and memory %.
    Optionally filters processes by name.
    """
    print_header("ACTIVE PROCESSES")
    print(Fore.YELLOW + f"{'PID':<10} {'Name':<30} {'CPU %':<10} {'Memory %':<10}")
    print("-" * 60)

    process_found = False  # To check if any processes are listed

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent'] or 0.00
            memory = proc.info['memory_percent'] or 0.00

            # Apply filtering if a name is provided
            if filter_name and filter_name.lower() not in name.lower():
                continue

            process_found = True
            print(f"{Fore.GREEN}{pid:<10}{Fore.WHITE}{name:<30}{Fore.MAGENTA}{cpu:<10.2f}{Fore.CYAN}{memory:<10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip processes we cannot access

    if not process_found:
        print(Fore.RED + "No processes found matching the given filter.")

def kill_process(pid):
    """
    Terminate a process by its PID.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(Fore.RED + Style.BRIGHT + f"Process {pid} ({process.name()}) terminated successfully.")
    except psutil.NoSuchProcess:
        print(Fore.YELLOW + f"Process with PID {pid} not found.")
    except psutil.AccessDenied:
        print(Fore.RED + f"Access denied: Cannot terminate process {pid}.")
    except Exception as e:
        print(Fore.RED + f"Error terminating process {pid}: {e}")
