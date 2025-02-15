#!/bin/bash

# Configuration
CPU_THRESHOLD=60  # Set CPU usage limit in percentage
MONITOR_INTERVAL=5  # Interval in seconds to check CPU usage
EMAIL="your-email@gmail.com"

# Function to check if a process is a system process
is_system_process() {
    local proc_name="$1"
    if [[ "$proc_name" == *"systemd"* || "$proc_name" == *"init"* || "$proc_name" == *"kthreadd"* || "$proc_name" == *"rcu"* ]]; then
        return 0  # System process (do not kill)
    fi
    return 1  # Not a system process
}

# Function to restart application process
restart_process() {
    local process_name="$1"
    pid=$(pgrep -f "$process_name")
    
    if [[ -n "$pid" ]]; then
        echo "Restarting application process: $process_name"
        kill -9 "$pid"
        sleep 2
        nohup "$process_name" &>/dev/null &
        echo "Application process restarted: $process_name"
    else
        echo "No process found with name: $process_name"
    fi
}

# Function to send an email alert
send_email() {
    local process_name="$1"
    local cpu_usage="$2"
    
    echo -e "High CPU Usage Detected!\n\nProcess: $process_name\nCPU Usage: $cpu_usage%" | mail -s "CPU Alert: $process_name" "$EMAIL"
    echo "Email alert sent for $process_name using $cpu_usage%"
}

# Monitor CPU usage
while true; do
    echo "Checking CPU usage..."
    
    # Get top CPU-consuming processes
    ps -eo pid,comm,%cpu --sort=-%cpu | awk -v threshold="$CPU_THRESHOLD" 'NR>1 {if ($3 > threshold) print $1, $2, $3}' | while read pid name cpu_usage; do
        echo "High CPU usage detected: $name using $cpu_usage%"

        if is_system_process "$name"; then
            send_email "$name" "$cpu_usage"
        elif [[ "$name" == "yourApp" ]]; then
            restart_process "$name"
        else
            echo "Killing non-essential process: $name"
            kill -9 "$pid"
        fi
    done
    
    sleep "$MONITOR_INTERVAL"
done

