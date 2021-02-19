import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Your computer name is: " + hostname)
print("Your computer IP Address is: " + IP)
