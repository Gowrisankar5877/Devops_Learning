import psutil
import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"  
SMTP_PORT = 587
EMAIL_FROM = "mgowrisankar5877@gmail.com"
EMAIL_PASSWORD = "P"
EMAIL_TO = "marepalligowrisankar999@gmail.com"

# List of application processes that should be restarted if killed
APPLICATION_PROCESSES = {
    "your_app_process": "/path/to/your/app_executable"
}

def send_email(process_name, cpu_usage):
    """Sends an email notification for system processes."""
    subject = f"High CPU Usage Alert: {process_name}"
    body = f"Process '{process_name}' is consuming {cpu_usage}% CPU."
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"Email sent regarding {process_name}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def restart_process(proc_name, proc_path):
    """Restarts a given process."""
    try:
        os.system(f"pkill {proc_name}")  # Kill the process
        print(f"Restarting {proc_name}...")
        os.system(proc_path)  # Restart the process
    except Exception as e:
        print(f"Failed to restart {proc_name}: {e}")

def monitor_cpu():
    """Monitors CPU usage and takes action if usage > 60%."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=2)  # Get CPU usage
        if cpu_usage > 60:
            print(f"High CPU Usage Detected: {cpu_usage}%")
            
            # Get process using most CPU
            processes = sorted(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']), 
                               key=lambda p: p.info['cpu_percent'], 
                               reverse=True)
            if processes:
                top_proc = processes[0]
                proc_name = top_proc.info['name']
                proc_pid = top_proc.info['pid']
                
                print(f"High CPU Process: {proc_name} (PID: {proc_pid})")
                
                # Check if it's a system process
                try:
                    proc = psutil.Process(proc_pid)
                    user = proc.username()
                    
                    if user in ["root", "system"]:  # Likely a system process
                        print(f"{proc_name} is a system process. Sending email alert.")
                        send_email(proc_name, cpu_usage)
                    elif proc_name in APPLICATION_PROCESSES:  # Application process
                        print(f"{proc_name} is an application process. Restarting it.")
                        restart_process(proc_name, APPLICATION_PROCESSES[proc_name])
                    else:
                        print(f"Killing {proc_name}.")
                        proc.kill()
                except Exception as e:
                    print(f"Error handling process: {e}")
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_cpu()
