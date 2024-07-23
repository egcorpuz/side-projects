import socket
import signal
import sys

HEADER = 64
PORT = 5050
#SERVER = "192.168.254.106"
SERVER = "192.168.1.58"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
def handle_name():
    usr_name = input()
    send(usr_name)
    pass

def main():
    
    handle_name()
    
    connected = True
    while connected:
        try:
            usr_input = input()
            send(usr_input)
            
            if usr_input == DISCONNECT_MESSAGE:
                send(DISCONNECT_MESSAGE)
                print("You have disconnected from the server.")
                connected = False
        except KeyboardInterrupt:
            send(DISCONNECT_MESSAGE)
            print("You have disconnected from the server.")
            sys.exit()
            
    return 0

if __name__ == "__main__":
    print(f"You have conencted to: {SERVER}.")
    print("Please input a name first:")
    main()
