# # cpu_monitor.py
# import psutil
# import os
# import time
# from sendemail import send_email

# # Configurations
# CPU_THRESHOLD = 35  # Set CPU usage limit in percentage
# MONITOR_INTERVAL = 1  # Interval in seconds to check CPU usage

# # Identify if a process is a system process
# def is_system_process(proc):
#     try:
#         exe_path = proc.exe().lower()
#         return "windows" in exe_path or "system32" in exe_path or "syswow64" in exe_path
#     except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
#         return False

# # Restart application process
# def restart_process(process_name):
#     try:
#         for proc in psutil.process_iter(attrs=['pid', 'name']):
#             if proc.info['name'].lower() == process_name.lower():
#                 os.kill(proc.info['pid'], 9)  # Force kill process
#                 print(f"Killed application process: {process_name}")
#                 time.sleep(2)
#                 os.system(f"start {process_name}")  # Restart process
#                 print(f"Restarted application process: {process_name}")
#     except Exception as e:
#         print(f"Error restarting process: {e}")

# # Monitor CPU usage
# def monitor_cpu():
#     while True:
#         try:
#             cpu_usage = psutil.cpu_percent(interval=1)
#             if cpu_usage > CPU_THRESHOLD:
#                 for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
#                     if proc.info['name'].lower() == "system idle process":
#                         continue  
#                     process_cpu = proc.cpu_percent(interval=0.1)
#                     if process_cpu > CPU_THRESHOLD:
#                         process_name = proc.info['name']
#                         print(f"High CPU usage detected: {process_name} using {process_cpu}%")

#                         if is_system_process(proc):
#                             send_email(process_name, process_cpu)
#                         else:
#                             os.kill(proc.info['pid'], 9)  # Kill unknown process
#                             print(f"Killed non-essential process: {process_name}")
#         except Exception as e:
#             print(f"Error monitoring CPU: {e}")
#         time.sleep(MONITOR_INTERVAL)

# if __name__ == "__main__":
#     monitor_cpu()



# cpu_monitor.py
import psutil
import os
import time
from sendemail import send_email

# Configurations
CPU_THRESHOLD = 60  # Set CPU usage limit in percentage
MONITOR_INTERVAL = 5  # Interval in seconds to check CPU usage

# List of processes that should NOT be killed (e.g., VS Code, Terminal, Python)
EXCLUDED_PROCESSES = {"code.exe", "cmd.exe", "powershell.exe", "python.exe", "pwsh.exe"}

# Identify if a process is a system process
def is_system_process(proc):
    try:
        exe_path = proc.exe().lower()
        return "windows" in exe_path or "system32" in exe_path or "syswow64" in exe_path
    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
        return False

# Restart application process
def restart_process(process_name):
    try:
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'].lower() == process_name.lower():
                os.kill(proc.info['pid'], 9)  # Force kill process
                print(f"Killed application process: {process_name}")
                time.sleep(2)
                os.system(f"start {process_name}")  # Restart process
                print(f"Restarted application process: {process_name}")
    except Exception as e:
        print(f"Error restarting process: {e}")

# Monitor CPU usage
def monitor_cpu():
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > CPU_THRESHOLD:
                for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
                    process_name = proc.info['name'].lower()
                    
                    if process_name in EXCLUDED_PROCESSES:
                        continue  # Skip killing VS Code, Terminal, Python, etc.

                    if proc.info['cpu_percent'] > CPU_THRESHOLD:
                        print(f"High CPU usage detected: {process_name} using {proc.info['cpu_percent']}%")
                        
                        if is_system_process(proc):
                            send_email(process_name, proc.info['cpu_percent'])
                        else:
                            os.kill(proc.info['pid'], 9)  # Kill unknown process
                            print(f"Killed non-essential process: {process_name}")
        except Exception as e:
            print(f"Error monitoring CPU: {e}")
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    monitor_cpu()
