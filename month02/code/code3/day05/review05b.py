from socket import *
#########tcp_client.py
sockfd = socket()
server_addr = ('127.0.0.1',1234)
sockfd.connect(server_addr)
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Server:",data.decode())
sockfd.close()

