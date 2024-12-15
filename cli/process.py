import psutil

import psutil

def list_processes(filter_name=None):
    """
    List all active processes with their PID, name, CPU %, and memory %.
    Optionally filters processes by name.
    """
    print(f"{'PID':<10} {'Name':<25} {'CPU %':<10} {'Memory %':<10}")
    print("-" * 60)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent'] or 0.00  # Default to 0.00 if None
            memory = proc.info['memory_percent'] or 0.00  # Default to 0.00 if None

            # Apply filtering if a name is provided
            if filter_name and filter_name.lower() not in name.lower():
                continue

            print(f"{pid:<10} {name:<25} {cpu:<10.2f} {memory:<10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip processes we cannot access


def kill_process(pid):
    """
    Terminate a process by its PID.
    """
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} ({process.name()}) terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
    except psutil.AccessDenied:
        print(f"Access denied: Cannot terminate process {pid}.")
    except Exception as e:
        print(f"Error terminating process {pid}: {e}")
