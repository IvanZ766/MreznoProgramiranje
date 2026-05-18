import socket
import subprocess
import platform

def check_ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception:
        return False

def print_remote_info(domain):
    if check_ping(domain):
        print(f"{domain} je dostupan ✅")
    else:
        print(f"{domain} nije dostupan ❌")

    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP adresa: {ip_address}")
    except socket.gaierror:
        print("Nije moguće dohvatiti IP adresu")

if __name__ == "__main__":
    domain = input("Unesite domenu (npr. google.com): ")
    print_remote_info(domain)