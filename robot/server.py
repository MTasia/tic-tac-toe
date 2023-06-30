import socket
import webbrowser

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip_port = ('192.168.153.224', 8000)
ip_port = ('192.168.1.36', 8000)

server.bind(ip_port)

server.listen()

while True:
    user, address = server.accept()

    print("connect")
    user.send("data to rapid".encode("utf-8"))


# print(robot.gethostbyname(robot.gethostname()))
# print(robot.gethostbyname_ex(robot.gethostname()))

