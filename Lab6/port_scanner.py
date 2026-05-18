import socket

# timeout
socket.setdefaulttimeout(0.5)

# unos hosta
host = input("Unesi host (npr. 127.0.0.1 ili scanme.nmap.org): ")

# unos port range
start_port = int(input("Unesi početni port: "))
end_port = int(input("Unesi završni port: "))

# provjera raspona
if start_port < 1 or end_port > 65535:
    print("Portovi moraju biti između 1 i 65535")
    exit()

print(f"\nSkeniram host: {host}")
print("Otvoreni portovi:\n")

# skeniranje
for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((host, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Nepoznat servis"

        print(f"Port {port} je OTVOREN ({service})")

    s.close()

print("\nSkeniranje završeno.")
