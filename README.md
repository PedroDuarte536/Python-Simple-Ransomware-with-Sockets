# Python-Simple-Ransomware-with-Sockets

server.py                     # attacker script
Target                        # victim's filesystem
      Teste                   # folder that will be affected
            importante.txt    # file that will be affected
      client.py               # script to run on victim's pc
      importante.txt          # file that will be affected
      
      
1 - Run server.py
2 - Run client.py
3 - All files in 'Target' and subsequent get encrypted (Fernet encryption)
4 - A file named 'README.txt' is created. When the script runs a second time this file will tell it he has to decrypt, not encrypt
4 - The server receives the key for decrypting and both scripts end
5 - Run server.py
6 - Run client.py
7 - This time server.py is asked to give the key
8 - Enter the key that was desplayed
9 - The files previously encrypted get decrypted
