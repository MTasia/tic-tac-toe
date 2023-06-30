import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print(socket.gethostbyname(socket.gethostname()))
# print(socket.gethostbyname_ex(socket.gethostname()))

# ip_port = ('192.168.153.224', 8000)
# ip_port = ('192.168.1.36', 8000)
ip_port = ('192.168.125.1', 1025)
# ip_port = ('127.0.0.1', 1025)

client.connect(ip_port)

res = client.recv(1024)
print(res)

while True:
    print("input data to rapid: ")
    data = input()
    client.send(data.encode())
    time.sleep(5)