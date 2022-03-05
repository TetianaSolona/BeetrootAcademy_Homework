import socket
from multiprocessing import Process


def server(conn):
    while True:
        data = conn.recv(1024)
        print(f'Receive data: {data}')
        if not data:
            break
        else:
            conn.sendall(data)
    conn.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 6005))
sock.listen(2)

while True:
    conn, add = sock.accept()
    process = Process(target=server, args=(conn,))
    process.start()