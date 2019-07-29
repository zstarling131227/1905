# ######http_test.py
"""
http 请求响应测试
"""
# from socket import *
# sockfd=socket()
# addr=('127.0.0.1',1234)
# sockfd.bind(addr)
# sockfd.listen(4)
#
# c,addr=sockfd.accept()
# print("Connect from",addr)
# data=c.recv(4096)
# print(data)
#
# response="""HTTP/1.1 200 OK
# Content-Type:text/html
#
# <h1>Hello World</h1>
# Hello World
# """
# c.send(response.encode())
# sockfd.close()
# c.close()
############运行该代码后直接在网页中输入＇127.0.0.1：1234＇回车则输出结果．

########struct
##将一组数据进行打包和解压操作
# import struct
# st=struct.Struct("i4sf")#######i4sf为参数格式
# # data=st.pack(1,b"lily",1.65)
# data=st.pack(1,"王八蛋".encode(),1.65)
# # data=st.pack(1,b"lily",1.65)####第二个参数lily长度超过４个，例zhang，则值截取４位．不足４位则补０
# print(data)
# data1=st.unpack(data)
# print(data1)
#####另外一种写法
# data=struct.pack("i4sf",1,"王八蛋".encode(),1.65)
# print(data)
# data1=struct.unpack("i4sf",data)
# print(data1)


#######练习
'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''
#############(自己写)struct_send(客户端)
# import struct
# from socket import *
# st=struct.Struct("i32sif")
# sockfd=socket(AF_INET,SOCK_DGRAM)
# addr=("127.0.0.1",8888)
# while True:
#     print("--------------")
#     id=int(input("ID:"))
#     if not id:
#         break
#     name=input("name:").encode()
#     age=int(input("age:"))
#     hight=float(input("hight:"))
#     # info=struct.pack("i7sf",age,name.encode(),hight)
#     # info=st.pack(ID,age,name.encode(),hight)
#     info=st.pack(id,name,age,hight)
#     sockfd.sendto(info,addr)
# sockfd.close()

# #############struct_send#############将字符串转换为字节串在ｗｈｉｌｅ中
# import struct
# from socket import *
# st=struct.Struct("i32sif")
# sockfd=socket(AF_INET,SOCK_DGRAM)
# addr=("127.0.0.1",8888)
# while True:
#     print("--------------")
#     id=int(input("ID:"))
#     if not id:
#         break
#     name=input("name:")
#     age=int(input("age:"))
#     hight=float(input("hight:"))
#     info=st.pack(id,name.encode(),age,hight)#############可以在此处将字符串转换为字节串
#     sockfd.sendto(info,addr)
# sockfd.close()

#############struct_send########struct.pack结构
# import struct
# from socket import *
# sockfd=socket(AF_INET,SOCK_DGRAM)
# addr=("127.0.0.1",8888)
# while True:
#     print("--------------")
#     id=int(input("ID:"))
#     if not id:
#         break
#     name=input("name:")
#     age=int(input("age:"))
#     hight=float(input("hight:"))
#     info=struct.pack("i32sif",id,name.encode(),age,hight)
#     sockfd.sendto(info,addr)
# sockfd.close()

###########老师讲struct_send.py
'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''
#
# from socket import *
# import struct
#
# # 数据格式定义
# st = struct.Struct('i32sif')
#
# # udp套接字
# s = socket(AF_INET,SOCK_DGRAM)
# ADDR = ('127.0.0.1',8888)
#
# while True:
#     print("============================")
#     id = int(input("ID:"))
#     name = input('Name:').encode()
#     age = int(input("Age:"))
#     score = float(input('Score:'))
#     # 打包数据发送
#     data = st.pack(id,name,age,score)
#     s.sendto(data,ADDR)




