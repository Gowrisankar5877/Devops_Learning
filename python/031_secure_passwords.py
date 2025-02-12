import hashlib
import os

def hash_password(password: str, salt_length: int = 16) -> str:
    salt = os.urandom(salt_length)  
    password_bytes = password.encode('utf-8')  
    hash_obj = hashlib.sha256(salt + password_bytes)  
    hashed_password = hash_obj.hexdigest()
    return f"{salt.hex()}:{hashed_password}"  

def verify_password(stored_password: str, provided_password: str) -> bool:
    salt, hashed_password = stored_password.split(":")  
    salt_bytes = bytes.fromhex(salt)  
    provided_hash = hashlib.sha256(salt_bytes + provided_password.encode('utf-8')).hexdigest()
    return provided_hash == hashed_password  
  
user_password = "securepassword123"
stored_hash = hash_password(user_password)
print(f"Stored Hash: {stored_hash}")
is_valid = verify_password(stored_hash, "securepassword123")
print("Password Verified:" if is_valid else "Invalid Password")
