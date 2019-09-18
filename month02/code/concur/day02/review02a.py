# 聊天室(看架构图)
#######chat_server.py
from socket import *
import os, sys

ADDR = ("0.0.0.0", 1234)
user = {}

def do_login(sockfd, name, address):
    if name in user or '管理员' in name:
        sockfd.sendto("该用户存在".encode(), address)
        return
    sockfd.sendto(b'ok', address)
    msg = "\n欢迎'%s'进入聊天室" % name
    for i in user:
        sockfd.sendto(msg.encode(), user[i])
    user[name] = address


def do_chat(sockfd, name, text):
    msg = "\n%s:%s" % (name, text)
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(), user[i])


def do_quit(sockfd, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(), user[i])
        else:
            sockfd.sendto(b'EXIT', user[i])
    del user[name]


def do_request(sockfd):
    while True:
        data, address = sockfd.recvfrom(1024)
        tmp = data.decode().split(" ")
        if tmp[0] == "L":
            do_login(sockfd, tmp[1], address)
        if tmp[0] == "C":
            text = " ".join(tmp[2:])
            do_chat(sockfd, tmp[1], text)
        if tmp[0] == "Q":
            do_quit(sockfd, tmp[1])


def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            sockfd.sendto(msg.encode(), ADDR)
    else:
        do_request(sockfd)

# main()

####################process1.py
"""
multiprocessing 模块创建进程
1. 编写进程函数
2. 生产进程对象
3. 启动进程
4. 回收进程
"""
# import multiprocessing as mp
# from time import sleep
# def fun():
#     print("开始一个进程")
#     sleep(5)
#     print("字进程结束")
# p=mp.Process(target=fun)
# p.start()
# p.join()
# p.join(2)
"""
与上述三行代码等同：
pid=os.fork()
if pid==0:
 fun()
 os.exit()
else:
 os.wait()
"""
# a=1
# # 进程函数
# def fun():
#     print("开始一个进程")
#     sleep(2)
#     global a
#     print('a = ',a)
#     a = 10000
#     print("子进程结束")

# # 创建进程对象
# p = mp.Process(target = fun)
# p.start() # 启动进程

# # 父进程事件
# sleep(3)
# print("父进程干点事")
#
# p.join() # 回收进程
# print('a:',a)

##########process2.py
"""
multiprocessing 创建多个进程
"""
# from multiprocessing import Process
# import os

# def th1():
#     sleep(3)
#     print("吃饭")
#     print(os.getppid(), "--", os.getpid())

# def th2():
#     sleep(2)
#     print("睡觉")
#     print(os.getppid(), "--", os.getpid())

# def th3():
#     sleep(4)
#     print("打豆豆")
#     print(os.getppid(), "--", os.getpid())

# things = [th1, th2, th3]
# jobs = []
# for th in things:
#     p = Process(target=th)
#     jobs.append(p)
#     p.start()
# for i in jobs:
#     i.join()

##########process3.py
"""
Proces 给进程函数传参
"""
# from multiprocessing import Process
# from time import sleep
# def worker(sec,name):
#     for i in range(3):
#         sleep(sec)
#         print("I am %s"%name)
#         print("I am working,,,")
# p=Process(target=worker,args=(2,"Baron"))
# p=Process(target=worker,kwargs={"name":"Baron","sec":2})
# p=Process(target=worker,args=(2,),kwargs={"name":"Baron"})
#
# p.start()
# p.join()

################process_attr.py
"""
进程对象属性
"""
# from multiprocessing import Process
# import time
# def tm():
#     for i in range(3):
#         time.sleep(2)
#         print(time.ctime())
# p=Process(target=tm,name="tarena")
# p.daemon=True
# p.start()
# print("Name:",p.name)
# print("PID:",p.pid)
# print("is_alive:",p.is_alive())

################pool.py
"""
进程池使用示例
"""
# from multiprocessing import Pool
# from time import sleep,ctime
# def tm(msg):
#     for i in range(3):
#         sleep(2)
#         print(ctime(),"--",msg)
# pool=Pool()
# for i in range(10):
#     # msg="ｔｅdt %d"%i
#     msg="tedt %d"%i
#     pool.apply_async(func=tm,args=(msg,))
# pool.close()
# pool.join()

