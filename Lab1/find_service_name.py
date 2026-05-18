import socket

user_input = input("unesite portove odvojene zarezom")

ports = [int(p.strip()) for p in user_input.split(",")]

for port in ports:
    try:
        service = socket.getservbyport(port)
        print(f"Port {port}: {service}")
    except OSError:
        print(f"Port {port}: kriva usluga")