import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8005))
data = b'Hello'
sock.sendall(data)
data = sock.recv(1024)
print(data)
sock.close()