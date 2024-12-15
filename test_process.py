from cli.process import list_processes, kill_process

# List all processes
print("Listing all processes:")
list_processes()

# Filter processes by name
print("\nListing processes with 'python' in the name:")
list_processes(filter_name="python")

# Kill a process (replace 1234 with an actual PID)
try:
    pid_to_kill = int(input("\nEnter PID of the process to kill: "))
    kill_process(pid_to_kill)
except ValueError:
    print("Invalid PID. Please enter a valid number.")
