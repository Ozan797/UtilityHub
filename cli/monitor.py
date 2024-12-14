import psutil

def get_cpu_usage():
    """Displays CPU usage percentage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

