import socket

HOST = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    while True:
        msg = input("Enter message (exit): ")

        if msg == "exit":
            break

        s.sendto(msg.encode(), (HOST, PORT))
        data, _ = s.recvfrom(1024)

        print("Server:", data.decode())
