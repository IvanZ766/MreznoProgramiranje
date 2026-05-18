import socket

HOST = "localhost"
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

msg = input("Unesite poruku: ")

sock.sendall(msg.encode())
data = sock.recv(1024)

print("Odgovor:", data.decode())

sock.close()
