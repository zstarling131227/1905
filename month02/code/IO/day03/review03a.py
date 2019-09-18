############客户端代码tcp_client.py
"""
tcp_client.py 　ｔｃｐ客户端流程
重点代码
"""
# from socket import *
# sockfd=socket()
# server_addr=('127.0.0.1',1234)
# sockfd.connect(server_addr)
# while 1:
#     data1=input('message:')
#     if data1=='quit':
#         break
#     sockfd.send(data1.encode())
#     data1=sockfd.recv(1024)
#     print("server:",data1.decode())
# sockfd.close()

#######stick_recv.py
"""
粘包演示
"""
# from socket import *
# from time import sleep
#
# sockfd = socket()
# sockfd.bind(('0.0.0.0', 8889))
# sockfd.listen(5)
# connfd,addr = sockfd.accept()
#
# while True:
#     data = connfd.recv(1024)
#     if not data:
#         break
#     print(data.decode())

###########send_file.py练习
# from socket import *
# sockfd=socket()
# server_addr=('127.0.0.1',1234)
# sockfd.connect(server_addr)
# filename=input("请输入文件名：")
# f=open(filename,'rb')
# while 1:
#     data=f.read()
#     if not data:
#         break
#     sockfd.send(data)
#     data1=sockfd.recv(1024)
#     print("server:",data.decode())
# f.close()
# sockfd.close()


##########udp_client.py
"""
udp_client.py  udp客户端流程
重点代码
"""
# from socket import *
# ADDR = ('127.0.0.1',1234)
# sockfd=socket(AF_INET,SOCK_DGRAM)
# while 1:
#     data=input("message:")
#     if not data:
#         break
#     sockfd.sendto(data.encode(),ADDR)
#     msg,addr=sockfd.recvfrom(1024)
#     print("FROM server:",msg.decode())
# sockfd.close()

##############练习
###########word_client.py（发现和展示请求结果）
# from socket import *
# sockfd=socket(AF_INET,SOCK_DGRAM)
# # addr=('176.23.4.105',1111)#########链接别人作为服务端时，改变的是客户端的ａｄｄｒ,改为别人的IP地址和端口．且别人的ｉｐ改为００００或自己本身的ＩＰ
# addr=('127.0.0.1',1234)#########链接自己作为服务端
# while True:
#     data=input("请输入单词：")
#     if not data:
#         break
#     sockfd.sendto(data.encode(),addr)
#     msg,addr=sockfd.recvfrom(1024)
#     print("from server:",msg)
# sockfd.close()

##########sock_attr.py
"""
套接字属性介绍
"""
# from socket import *
# s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('172.40.91.108',1234))
# s.listen(4)
# c,addr=s.accept()
# print("地址类型:",s.family)
# print("套接字类型:",s.type)
# print("绑定地址：",s.getsockname())
# print("文件描述符：",s.fileno())
# # 链接套接字调用　结果同accept返回的ａｄｄｒ
# print("连接端地址:",c.getpeername())
# c.recv(1024) #　提供阻塞

###########broadcast_recv.py
"""
广播接收
1. 创建udp套接字
2. 设置套接字可以发送接收广播　（setsockopt）
3. 选择接收的端口
4. 接收广播
"""
# from socket import *
# sockfd=socket(AF_INET,SOCK_DGRAM)
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sockfd.bind(('0.0.0.0',1234))
# while 1:
#     msg,addr=sockfd.recvfrom(1024)
#     print(msg.decode())

##################http_test.py(看图http.png)
"""
http 请求响应测试
"""
from socket import *
sockfd=socket()
addr=('127.0.0.1',1234)
sockfd.bind(addr)
sockfd.listen(4)
msg,addr=sockfd.accept(1024)
data=msg.recv(4089)
print(data)
sockfd.close()
msg.close()
