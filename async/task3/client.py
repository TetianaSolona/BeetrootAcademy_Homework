import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8001))
data = b'With Ukraine in heart'
sock.sendall(data)
print(sock.recv(1024))
sock.close()