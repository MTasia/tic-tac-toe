import socket


def init_client(client):
    ip_port = ('192.168.125.1', 1025)
    client.connect(ip_port)
    return "We can start"


def send_data(client, data):
    client.send(data.encode())
    print('send')


def get_data(client):
    get = client.recv(1024)
    return get
