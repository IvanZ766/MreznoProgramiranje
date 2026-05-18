import socket

socket.setdefaulttimeout(0.5)


def scan(host, start_port, end_port):

    print(f"\nOtvoreni portovi na {host}:\n")

    for port in range(start_port, end_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Nepoznat servis"

            print(f"- {port} ({service})")

        s.close()


# INPUT
host = input("Unesi host (127.0.0.1 ili scanme.nmap.org): ")

start_port = int(input("Unesi početni port: "))
end_port = int(input("Unesi završni port: "))

# VALIDACIJA
if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Neispravan raspon portova (1-65535)")
    exit()

scan(host, start_port, end_port)

