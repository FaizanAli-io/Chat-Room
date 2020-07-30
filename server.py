import socket, threading

HEADER = 16
PORT = 8000
FORMAT = 'utf-8'
DISCONNECT = '$!#^'
SERVER = '192.168.100.58'
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(conn, addr):
    print(clients)
    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        if msg:
            if msg[-len(DISCONNECT):] == DISCONNECT: connected = False
            print(msg)
            for connect in clients:
                try:
                    connect.send(msg.encode(FORMAT))
                except:
                    clients.remove(connect)
    conn.close()
    clients.remove(conn)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Active Users: " + str(threading.activeCount() - 1))

print(f"running on {SERVER}...")
start()