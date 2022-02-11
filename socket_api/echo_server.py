import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(1)
conn, addr = sock.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        # data = encrypted(data)
        if not data:
            break
        else:
            conn.sendall(data)
    conn.close()
