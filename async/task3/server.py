import socket
import asyncio


async def server(conn):
    while True:
        data = await conn.recv(1024)
        print(f'Receive data: {data}')
        if not data:
            break
        else:
            await conn.sendall(data)
    conn.close()


async def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))
    sock.listen(4)

    while True:
        conn, add = await sock.accept()
        await server(conn)

if __name__ == '__main__':
    asyncio.run(main())
