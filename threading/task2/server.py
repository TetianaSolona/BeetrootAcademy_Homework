import socket
import threading

def handle(conn):
    while True:
        data = conn.recv(1024)
        print(f'Receive: {data}')
        if not data:
            break
        else:
            conn.sendall(data)
    conn.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8005))
sock.listen(2)

while True:
    conn, addr = sock.accept()
    thread = threading.Thread(target=handle, args=(conn,))
    thread.start()