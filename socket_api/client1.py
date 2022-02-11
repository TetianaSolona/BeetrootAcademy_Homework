import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
massage = b'Massage to UDP server'
client.sendto(massage, ('127.0.0.1', 8001))
data, addr = client.recvfrom(4096)
print(data.decode('utf-8'))
client.close()