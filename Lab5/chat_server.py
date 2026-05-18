import selectors
import socket
import time
import threading

sel = selectors.DefaultSelector()
clients = {}  # conn -> name

HOST = 'localhost'
PORT = 65433

log_file = "log.txt"


def log(msg):
    with open(log_file, "a") as f:
        f.write(msg + "\n")


def print_user_count():
    last = -1
    while True:
        time.sleep(10)
        current = len(clients)

        if current != last:
            last = current
            msg = f"[INFO] Active users: {current}"
            print(msg)
            log(msg)


# start background thread
threading.Thread(target=print_user_count, daemon=True).start()


lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)

sel.register(lsock, selectors.EVENT_READ)

print(f"[CHAT SERVER] Listening on {HOST}:{PORT}")
log("[START] Server started")


def broadcast(message, exclude=None):
    for c in clients:
        if c != exclude:
            try:
                c.sendall(message.encode())
            except:
                pass


while True:
    events = sel.select()

    for key, _ in events:

        # NEW CONNECTION
        if key.fileobj == lsock:
            conn, addr = lsock.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ)
            clients[conn] = {"addr": addr, "name": None}
            log(f"[CONNECT] {addr}")

        else:
            conn = key.fileobj
            data = conn.recv(1024)

            if not data:
                name = clients[conn]["name"]
                log(f"[DISCONNECT] {name}")
                sel.unregister(conn)
                conn.close()
                del clients[conn]
                continue

            msg = data.decode().strip()

            # FIRST MESSAGE = NAME
            if clients[conn]["name"] is None:
                clients[conn]["name"] = msg
                log(f"[LOGIN] {msg}")
                conn.sendall("Welcome!".encode())
                continue

            name = clients[conn]["name"]

            # COMMAND /users
            if msg == "/users":
                user_list = ", ".join([c["name"] for c in clients.values() if c["name"]])
                conn.sendall(f"Online: {user_list}".encode())
                continue

            # NORMAL MESSAGE
            full_msg = f"{name}: {msg}"
            print(full_msg)
            log(full_msg)
            broadcast(full_msg, exclude=conn)

