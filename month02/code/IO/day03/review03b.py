#####tcp_server.py(自己写)
"""
tcp_server.py  tcp套接字服务端流程
重点代码

注意：　功能性代码，注重流程和函数使用
"""
# import  socket
# sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sockfd.bind(("127.0.0.1",1234))
# sockfd.listen(5)
# while 1:
#     print("waiting for connect...")
#     try:
#         connfd,addr=sockfd.accept()
#         print("Connect from",addr)
#         f = open("copy_filename", 'wb')
#     except KeyboardInterrupt:
#         print("服务器退出")
#         break
#     except Exception as e:
#         print(e)
#         continue
#     while 1:
#         data=connfd.recv(1024)
#         if not data:
#             break
#         f.write(data)
#         print("收到：",data.decode())
#         print("收到：",data)
#         n=connfd.send(b'Thanks')
#         print("发送%d个字节"%n)
#     f.close()
#     connfd.close()
# sockfd.close()

#######stick_send.py##########粘包服务端
# from socket import *
# from time import sleep
#
# sockfd = socket()
# server_addr = ('127.0.0.1',8889) #服务端地址
# sockfd.connect(server_addr)
#
# for i in range(10):
#     sockfd.send(b'msg#')

##########recv_file.py老师讲
"""
练习：　将一个文件从客户端发送到服务端保存
　　　  文件可能是文本类型也可能是二进制文件
"""
# import  socket
# sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sockfd.bind(("127.0.0.1",1234))
# sockfd.listen(5)
# c,addr = sockfd.accept()
# print("Connect from",addr)
# f = open('copy','wb')
# while True:
#     data = c.recv(1024)
#     if not data:
#         break
#     f.write(data)
# f.close()
# c.close()
# sockfd.close()

######udp_server.py
"""
udp_server.py ｕｄｐ套接字服务端流程
重点代码
"""
# from socket import *
# sockfd=socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(('127.0.0.1',1234))
# while True:
#     data,addr=sockfd.recvfrom(1024)
#     print("收到的消息：",data.decode())
#     sockfd.sendto(b'wangbadan',addr)
#
# sockfd.close()


############练习
############word_server.py（服务端提供逻辑和数据处理）
# def dictionary(word):
    # f = open("dict.txt", "r")
    # for i in f:
    #     a = i.index(" ")
    #     if word < i[:a]:#########TypeError: '<' not supported between instances of 'bytes' and 'str'
    #         f.close()
    #         return "没有找到该单词"
    #     if word==i[:a]:
    #         f.close()
    #         return  i
    # else:
    #     f.close()
    #     raise ValueError("the word is not existing.")
# # print(dictionary('abandon'))
# from socket import *
# sockfd=socket(AF_INET,SOCK_DGRAM)
# # sockfd.bind(('0.0.0.0',1234))###被不同台的客户端连接时改为００００
# sockfd.bind(('0.0.0.0',1234))
# while True:
#     data,addr=sockfd.recvfrom(1024)
#     sockfd.sendto(dictionary(data.decode()).encode(),addr)
# sockfd.close()

###########boradcast_send.py
"""
广播发送
1. 创建ｕｄｐ套接字
2. 设置可以发送广播
3. 循环向广播地址发送
"""
from socket import *
import time
dest=('176.23.4.102',1234)
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
data = input("<<")
while 1:
    time.sleep(2)
    sockfd.sendto(data.encode(),dest)









