import socket

ip = "8.8.8.8"

try:
    hostname = socket.gethostbyaddr(ip)
    print(f"Hostname za {ip}: {hostname[0]}")
except socket.herror:
    print("nije  moguce dohvatiti hostname")

print("\n Portoovi:")

ports = [80, 443, 22, 53]

for port in ports:
    try:
        service = socket.getservbyport(port)
        print(f"Port {port}: {service}")
    except OSError:
        print(f"Port {port}: kriva usluga")