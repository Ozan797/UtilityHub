import psutil

def get_cpu_usage():
    """Displays CPU usage percentage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")


def get_memory_usage():
    """Get memory usage"""
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2) # Convert bytes to GB
    used_memory = round(memory.used / (1024 ** 3) , 2)
    free_memory = round(memory.available / (1024 ** 3), 2)
    print(f"Memory Usage: {used_memory} GB used / {total_memory} GB total (Free: {free_memory} GB)")

    
    
def get_disk_usage():
    """Get disk usage"""
    disk = psutil.disk_usage("/")
    total_disk = round(disk.total / (1024 ** 3), 2)
    used_disk = round(disk.used / (1024 ** 3), 2)
    free_disk = round(disk.free / (1024 ** 3), 2)
    print(f"Disk Usage: {used_disk} GB used / {total_disk} GB total (Free: {free_disk} GB)")