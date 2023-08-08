import os
import shutil
import psutil
import platform

# Define source and destination directories for file organization
source_directory = 'source_folder'
destination_directory = 'destination_folder'

# Organize files from source to destination directory
def organize_files():
    try:
        for filename in os.listdir(source_directory):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
    except Exception as e:
        print(f"Error: {e}")

# Check system health
def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    system_info = platform.uname()

    report = f"System Health Report:\n"
    report += f"CPU Usage: {cpu_usage}%\n"
    report += f"Memory Usage: {memory_usage}%\n"
    report += f"Disk Usage: {disk_usage}%\n"
    report += f"System: {system_info.system}\n"
    report += f"Node Name: {system_info.node}\n"
    report += f"Release: {system_info.release}\n"
    report += f"Version: {system_info.version}\n"
    report += f"Machine: {system_info.machine}\n"
    report += f"Processor: {system_info.processor}\n"

    return report

if __name__ == '__main__':
    organize_files()
    health_report = check_system_health()
    print(health_report)
