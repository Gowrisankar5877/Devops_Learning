#!/bin/bash

# Configurations
CPU_THRESHOLD=60   # CPU usage limit in percentage
MONITOR_INTERVAL=5 # Interval in seconds to check CPU usage
EXCLUDED_PROCESSES=("code.exe" "cmd.exe" "python.exe" "pwsh.exe")  # Do not kill
RESTART_PROCESSES=("chrome.exe" "notepad.exe" "powershell.exe")  # Restart these after killing
EMAIL="mgowrisankar5877@gmail.com"  # Replace with your email

# Function to check if a process should be excluded
should_exclude() {
    local process=$1
    for excluded in "${EXCLUDED_PROCESSES[@]}"; do
        if [[ "$process" == "$excluded" ]]; then
            return 0  # Found in exclusion list
        fi
    done
    return 1  # Not in exclusion list
}

# Function to check if a process should be restarted
should_restart() {
    local process=$1
    for restart in "${RESTART_PROCESSES[@]}"; do
        if [[ "$process" == "$restart" ]]; then
            return 0  # Found in restart list
        fi
    done
    return 1  # Not in restart list
}

# Function to send email alert (Using PowerShell for Windows)
send_alert() {
    local cpu_usage=$1
    powershell.exe -Command "
        \$SMTPServer = 'smtp.gmail.com';
        \$SMTPPort = 587;
        \$Username = 'mgowrisankar5877@gmail.com';
        \$Password = ConvertTo-SecureString 'mail password' -AsPlainText -Force;
        \$Credential = New-Object System.Management.Automation.PSCredential (\$Username, \$Password);
        \$Message = New-Object System.Net.Mail.MailMessage;
        \$Message.From = 'mgowrisankar5877@gmail.com';
        \$Message.To.Add('marepalligowrisankar999@gmail.com');
        \$Message.Subject = '⚠️ High CPU Usage Alert';
        \$Message.Body = 'CPU usage exceeded threshold: ${cpu_usage}% on $(hostname) at $(date)';
        \$SMTP = New-Object Net.Mail.SmtpClient (\$SMTPServer, \$SMTPPort);
        \$SMTP.EnableSsl = \$true;
        \$SMTP.Credentials = \$Credential;
        \$SMTP.Send(\$Message);
    "
}

# Function to restart a process
restart_process() {
    local process=$1
    echo "🔄 Restarting $process..."
    nohup "$process" &>/dev/null &
}

# Function to monitor CPU usage
monitor_cpu() {
    while true; do
        CPU_USAGE=$(wmic cpu get loadpercentage | awk 'NR==2 {print $1}')
        
        if [[ -n "$CPU_USAGE" && $CPU_USAGE -gt 0 ]]; then
            echo "Current CPU Usage: $CPU_USAGE%"
        else
            echo "⚠️ Could not retrieve CPU usage."
            CPU_USAGE=0
        fi

        if [[ $CPU_USAGE -gt $CPU_THRESHOLD ]]; then
            echo "⚠️ High CPU detected: $CPU_USAGE%. Checking processes..."
            send_alert "$CPU_USAGE"  # Send email alert

            # Get processes consuming CPU > CPU_THRESHOLD
            wmic process get Name,ProcessId,CommandLine | awk 'NR>1 {print $1, $2}' | while read -r process pid; do
                if [[ -z "$process" || -z "$pid" ]]; then
                    continue  # Skip empty lines
                fi

                should_exclude "$process"
                if [[ $? -eq 0 ]]; then
                    echo "✅ Skipping: $process (Protected)"
                else
                    should_restart "$process"
                    if [[ $? -eq 0 ]]; then
                        echo "🔄 Restarting $process (PID: $pid)"
                        taskkill /F /PID "$pid"
                        restart_process "$process"
                    else
                        echo "❌ Killing non-essential process: $process (PID: $pid)"
                        taskkill /F /PID "$pid"
                    fi
                fi
            done
        fi
        sleep "$MONITOR_INTERVAL"
    done
}

# Start Monitoring
monitor_cpu
