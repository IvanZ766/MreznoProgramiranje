import socket

HOST = "127.0.0.1"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print("Connected")

    while True:
        msg = input("Message (exit): ")

        if msg == "exit":
            break

        s.sendall(msg.encode())
        print("Server:", s.recv(1024).decode())

