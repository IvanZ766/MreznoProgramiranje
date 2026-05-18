import socket

HOST = 'localhost'
PORT = 65433

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

name = input("Username: ")
sock.sendall(name.encode())

print("Chat started. Commands: /users")

while True:
    msg = input("> ")
    sock.sendall(msg.encode())

    data = sock.recv(1024)
    print(data.decode())
