import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(con, addr):
    print(f"new connection created by {addr}")
    connected = True
    while connected:
        msg_length = con.recv(HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = con.recv(msg_length).decode("utf-8")
            if msg == "disconnected":
                connected = False
            print(f"{addr}: {msg}")
            con.send(("msg received").encode("utf-8"))
    con.close()

def start():
    server.listen()
    while True:
        con, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(con, addr))
        thread.start()
        print(f"active connections: {threading.active_count() - 1}")

print(f"server is starting to listen on port {PORT}")
start()
