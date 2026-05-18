import socket
import datetime
from local_machine_info import print_machine_info

HOST = "0.0.0.0"
PORT = 6000

print(datetime.datetime.now())
print_machine_info()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("[TCP SERVER] Listening...")

    while True:
        conn, addr = s.accept()

        with conn:
            print("Client:", addr)

            while True:
                data = conn.recv(1024)
                if not data:
                    break

                msg = data.decode()

                print(datetime.datetime.now(), msg, addr)

                if msg == "vaše_ime_prezime":
                    conn.sendall("Unos nije podržan.".encode())
                else:
                    conn.sendall(msg.encode())
