import socket
import threading
from datetime import datetime

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    usr_name = conn.recv(HEADER).decode(FORMAT)
    usr_name = int(usr_name)
    usr_name = conn.recv(HEADER).decode(FORMAT)
    print(f"[NEW CONNECTION] {addr}: User {usr_name} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            now = datetime.now()
            t_now = now.strftime("%m/%d/%Y, %H:%M:%S")     
            print(f"{t_now} {usr_name}: {msg}")
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listeing on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

def main():
    start()
    return 0
	
if __name__ == "__main__":
    print("[STARTING SERVER] server is starting...")
    main()
