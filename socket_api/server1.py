import socket
#socket with udp protocol
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('127.0.0.1',8001))

while True:
    data, addr = udp_socket.recvfrom(4096)
    print('Receive data', data.decode('utf-8'))
    massage = b'Massage from UDP server'
    udp_socket.sendto(massage,addr)
