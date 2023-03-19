# import socket

# def main():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     host = 'localhost'
#     port = 80
#     sock.connect((host, port))
#     print('Port it is Open') else print('port is closed')
#     sock.close()

# if __name__ == '__main__':
#     main()

#ChatGPT:
# import socket

# ip = input("Enter IP address: ")
# port = int(input("Enter port number: "))

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(5)

# result = sock.connect_ex((ip, port))
# #why zero, when zero is false?
# if result == 0:
#     print("Port is open")
# else:
#     print("Port is closed")

# sock.close()

#devPORTscanner

# import socket
# #socket allows low-level network communication
# # Get input from user
# target = input("Enter IP address to scan: ")
# start_port = int(input("Enter starting port number: "))
# end_port = int(input("Enter ending port number: "))

# # Loop through each port and try to connect to it
# for port in range(start_port, end_port+1):
#     #socket.AF_INET:a ipv4,SOCK_STEAM:a tcp socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #spendOnly1sec
#     sock.settimeout(1)
#     #if 0=successConnect,
#     result = sock.connect_ex((target, port))
#     if result == 0:
#         print(f"Port {port}: Open")
#     sock.close()

###PasswordCracker
import hashlib

def crack_password(hash, password_list):
    for password in password_list:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if hash == hashed_password:
            print("Password found: ", password)
            return

password_hash = "c5e478d59288c841aa6b73a0f5a502d94aab42df2c0e5d6b5c6fcd8965f745ba"
password_list = ["password", "123456", "qwerty", "letmein", "monkey", "admin", "welcome", "password1"]
crack_password(password_hash, password_list)