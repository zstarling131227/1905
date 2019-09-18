#############tcp_server
from socket import *
sockfd = socket(AF_INET, SOCK_STREAM, proto=0)
sockfd.bind(('127.0.0.1', 1234))
sockfd.listen(5)
print("waiting for connect...")
connfd, addr = sockfd.accept()
data = sockfd.recv(1024)
n = connfd.send(data)
print("发送%d字节", n)
connfd.close()
sockfd.close()

#############tcp_client
sockfd1 = socket(AF_INET, SOCK_STREAM)  ###默认值可忽略
sockfd1.connect(('127.0.0.1', 1234))
while 1:
    data = input(">>")
    if not data:
        break
    sockfd1.send(data.encode())
    data = sockfd1.recv(1024)
    print("Server:", data.decode())
sockfd1.close()


#############udp_server
sockfd2=socket(AF_INET,SOCK_DGRAM)
sockfd2.bind(('127.0.0.1',1234))
data,addr=sockfd2.recvfrom(1024)
sockfd2.sendto(data,addr)
sockfd2.close()


#############udp_client
sockfd3=socket(AF_INET,SOCK_DGRAM)
addr='127.0.0.1',1234
data=input(">>")
sockfd3.sendto(data.encode(),addr)
msg,addr=sockfd3.recvfrom(1024)
print("server:",msg.decode())
sockfd3.close()