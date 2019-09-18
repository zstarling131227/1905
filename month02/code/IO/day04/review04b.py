#######练习
'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''
###自己写
#############struct_recv（服务端）
# from socket import *
# import struct
# st=struct.Struct("i32sif")
# sockfd=socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(("127.0.0.1",8888))
# g = open("student01.txt", 'a')
# while 1:
#     data,addr=sockfd.recvfrom(1024)
#     data = st.unpack(data)
#     info="%d %-10s %d %.1f\n" % data
#     g.write(info)
#     g.flush()

# #############struct_recv#############将字符串转换为字节串在ｗｈｉｌｅ中
# from socket import *
# import struct
# st=struct.Struct("i32sif")
# sockfd=socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(("127.0.0.1",8888))
# g = open("student01.txt", 'a')
# while 1:
#     data,addr=sockfd.recvfrom(1024)
#     if not data:
#         break
#     data = st.unpack(data)
#     info = "%d   %-10s  %d  %.1f\n"%data
#     g.write(info)
#     g.flush()
# sockfd.close()


#############struct_recv########struct.pack结构
# from socket import *
# import struct
# sockfd=socket(AF_INET,SOCK_DGRAM)
# sockfd.bind(("127.0.0.1",8888))
# g = open("student01.txt", 'a')
# while 1:
#     data,addr=sockfd.recvfrom(1024)
#     if not data:
#         break
#     data = struct.unpack("i32sif",data)
#     info = "%d   %-10s  %d  %.1f\n"%data
#     g.write(info)
#     g.flush()
# sockfd.close()

###########老师讲struct_recv.py
'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''
#
# from socket import *
# import struct
#
# # 和客户端一致
# st = struct.Struct('i32sif')
#
# # udp套接字
# s = socket(AF_INET,SOCK_DGRAM)
# s.bind(('127.0.0.1',8888))
#
# # 打开文件
# f = open('student.txt','a')
#
# while True:
#     data,addr = s.recvfrom(1024)
#     # (1,b'Lily',14,92.5)
#     data = st.unpack(data)
#
#     # 写入文件
#     info = "%d   %-10s  %d  %.1f\n"%data
#     f.write(info)
#     f.flush()



