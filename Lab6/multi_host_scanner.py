import socket

socket.setdefaulttimeout(0.5)


def scan_host(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            open_ports.append((port, service))

        s.close()

    return open_ports


# INPUT
hosts_input = input("Unesi hostove (odvoji zarezom, npr. 127.0.0.1,scanme.nmap.org): ")
hosts = [h.strip() for h in hosts_input.split(",")]

start_port = int(input("Početni port: "))
end_port = int(input("Završni port: "))

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Neispravan raspon portova")
    exit()


print("\n=== REZULTATI SKENIRANJA ===\n")

for host in hosts:
    print(f"\nHOST: {host}")
    print("-" * 30)

    open_ports = scan_host(host, start_port, end_port)

    if len(open_ports) == 0:
        print("Nema otvorenih portova")
    else:
        print("PORT   SERVIS")
        print("-" * 30)

        for port, service in open_ports:
            print(f"{port:<6} {service}")

