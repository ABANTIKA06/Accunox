import psutil
import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

def check_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"[{datetime.datetime.now()}] CPU usage is high: {cpu_percent}%")

def check_memory():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"[{datetime.datetime.now()}] Memory usage is high: {memory_percent}%")

def check_disk():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        print(f"[{datetime.datetime.now()}] Disk usage is high: {disk_percent}%")

def check_processes():
    num_processes = len(psutil.pids())
    if num_processes > PROCESS_THRESHOLD:
        print(f"[{datetime.datetime.now()}] Number of processes is high: {num_processes}")

def main():
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    main()