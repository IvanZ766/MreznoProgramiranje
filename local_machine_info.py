import socket

hostname = socket.gethostname()

try:
    local_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    local_ip = "Nije moguće dohvatiti IP adresu"

print(f"Ime računala: {hostname}")
print(f"Lokalna IP adresa: {local_ip}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9999))
    server_socket.listen(1)
    print("TCP server pokrenut na portu 9999...")
    
    conn, addr = server_socket.accept()
    print(f"Povezan klijent: {addr}")
    conn.sendall(b"Pozdrav s servera!\n")
    conn.close()

if __name__ == "__main__":
    start_server()