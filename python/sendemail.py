import smtplib
import os
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

# Configurations
ENCRYPTION_KEY_FILE = "key.key"
PASSWORD_FILE = "password.enc"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "mgowrisankar5877@gmail.com"
EMAIL_RECEIVER = "marepalligowrisankar999@gmail.com"

# Load or generate encryption key
def load_or_create_key():
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key
# Encrypt password and store
def encrypt_password(password):
    key = load_or_create_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    with open(PASSWORD_FILE, "wb") as enc_file:
        enc_file.write(encrypted_password)

# Decrypt stored password
def decrypt_password():
    key = load_or_create_key()
    cipher = Fernet(key)
    with open(PASSWORD_FILE, "rb") as enc_file:
        encrypted_password = enc_file.read()
    return cipher.decrypt(encrypted_password).decode()

# Send alert email
def send_email(process_name, cpu_usage):
    try:
        password = decrypt_password()
        msg = MIMEText(f"Alert! System process {process_name} is consuming high CPU: {cpu_usage}%")
        msg['Subject'] = "High CPU Usage Alert"
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, password)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")