import base64
import hashlib
import itertools

# Function to crack Cisco Type 7 passwords
def crack_type7_password(password_hash):
    password_hash = password_hash.strip()
    if password_hash.startswith('7'):
        password_hash = password_hash[1:]
    password = ""
    for i in range(0, len(password_hash), 2):
        password_char = int(password_hash[i:i+2], 16) ^ 0x42
        password += chr(password_char)
    print("Password: ", password)

# Function to crack Cisco Type 5 passwords
def crack_type5_password(password_hash, wordlist):
    with open(wordlist, "r") as f:
        for password in f:
            password = password.strip()
            salt = password_hash[:12]
            crypt_password = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
            if crypt_password == password_hash:
                print("Password found: ", password)
                return
    print("Password not found in wordlist")

# Example usage for cracking Type 7 password
password_hash = "073C5C5908090D"
crack_type7_password(password_hash)

# Example usage for cracking Type 5 password
password_hash = "eH1/wuXpXjJbGcHQ"
wordlist = "/path/to/wordlist.txt"
crack_type5_password(password_hash, wordlist)
