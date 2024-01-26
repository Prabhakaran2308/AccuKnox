import os
import subprocess

def print_colored(text, color):
    colors = {'green': '\033[92m', 'red': '\033[91m', 'end': '\033[0m'}
    print(colors.get(color, ''), text, colors['end'])

def check_cpu_usage(threshold):
    # Using 'top' command to get CPU usage, this is a Linux-specific solution
    cpu_usage = float(os.popen("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\([0-9.]*\)%* id.*/\\1/' | awk '{print 100 - $1}'").read().strip())
    if cpu_usage > threshold:
        print_colored(f"Warning: CPU usage is high at {cpu_usage}%", 'red')
    else:
        print_colored(f"CPU usage is at {cpu_usage}%, within normal limits.", 'green')

def check_memory_usage(threshold):
    # Using 'free' command to get memory usage, this is also Linux-specific
    memory_usage = float(os.popen("free | grep Mem | awk '{print $3/$2 * 100.0}'").read().strip())
    if memory_usage > threshold:
        print_colored(f"Warning: Memory usage is high at {memory_usage}%", 'red')
    else:
        print_colored(f"Memory usage is at {memory_usage}%, within normal limits.", 'green')

def check_disk_space(threshold):
    # Getting disk space usage for all mounted filesystems
    df_output_lines = subprocess.check_output(['df', '-h']).decode().split('\n')

    for line in df_output_lines[1:]:  # Skip the header line
        parts = line.split()
        if len(parts) > 5:  # Ensure it's a valid line
            filesystem, size, used, available, percent, mountpoint = parts
            usage = int(percent.strip('%'))
            if usage > threshold:
                print_colored(f"Warning: Disk usage is high on filesystem {filesystem} at {mountpoint} ({usage}%)", 'red')
            else:
                print_colored(f"Disk space usage on filesystem {filesystem} at {mountpoint} is {usage}%, within normal limits.", 'green')

def check_running_processes():
    # Counting the number of running processes
    try:
        processes = subprocess.check_output(['ps', '-e']).decode().split('\n')
        print_colored(f"Number of running processes: {len(processes) - 1}", 'green')
    except subprocess.CalledProcessError as e:
        print_colored("Failed to count running processes.", 'red')

def check_running_services():
    try:
        # Counting the number of active services using 'systemctl'
        output = subprocess.check_output(['systemctl', 'list-units', '--type=service', '--state=running']).decode()
        services = output.count('.service')
        print_colored(f"Number of active services: {services}", 'green')
    except subprocess.CalledProcessError as e:
        print_colored("Failed to count running services.", 'red')

def main():
    cpu_threshold = 80
    memory_threshold = 80
    disk_threshold = 80

    # Check system health
    check_cpu_usage(cpu_threshold)
    check_memory_usage(memory_threshold)
    check_disk_space(disk_threshold)
    check_running_processes()
    check_running_services()

if __name__ == "__main__":
    main()

