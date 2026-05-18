import socket

HOST = "0.0.0.0"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print("[UDP SERVER] Running...")

    while True:
        data, addr = s.recvfrom(1024)
        msg = data.decode()

        print("Received:", msg, "from", addr)

        s.sendto(f"OK: {msg}".encode(), addr)

