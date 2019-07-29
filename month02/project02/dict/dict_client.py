"""
dict 客户端

功能：根据用户输入发送请求，得到结果
模型：多进程 TCP并发
封装：函数
"""
from socket import *
import time,sys,getpass
HOST="127.0.0.1"
PORT=1234
ADDR=(HOST,PORT)
sockfd = socket()
sockfd.connect(ADDR)

def query(name):
    while True:
        word=input("单词：")
        if word=="##":
            break
        msg="Q %s %s"%(name,word)
        sockfd.send(msg.encode())
        data=sockfd.recv(2048).decode()
        print(data)

def do_hist(name):##（对应do_hist）
    msg = "H %s"%(name)
    sockfd.send(msg.encode()) # 发送请求

    ##接收问题
    data = sockfd.recv(128).decode()
    # print(data)
    if data=='ok':
        while True:
            data=sockfd.recv(1024).decode()
            if data=='##':###必须有结束标志
                break
            print(data)
    else:
        # print("您还没有查询记录")  ###对应c.send(b"failed")
        print(data)   ##对应c.send(("%s没有历史记录"%name).encode())


def do_hist1(name):##  代码问题：查询到没有历史记录时会有问题，无法退回到二级界面（对应do_hist1）
    msg = "H %s"%(name)
    sockfd.send(msg.encode())
    while  1:###if语句发送过来的语句没有空字符，while语句会无限执行，而不会执行else语句。或者而不会自动退出查询步骤。
        data = sockfd.recv(2048).decode()
        if data=="##":
            break
        print(data)
    else:
        print(data)
        return

def do_hist3(name): ###要找到标志表示结束，退回以及界面（对应do_hist1）
    msg = "H %s"%(name)
    sockfd.send(msg.encode())
    while  1:###if语句会无限执行
        data = sockfd.recv(2048).decode()
        if data=="##":
            break
        elif "历史记录" in data:###结束标志
            print(data)
            break
        print(data)


def login_next(name):
    while True:
        print("""
        ==============query===============
        1.查单词    2.查询历史记录    3.注销
        ==================================
        """)
        cmd = input("请输入命令：")
        if cmd == "1":
            query(name)
        elif cmd == "2":
            do_hist(name)
        elif cmd == "3":
            # break
            return ##break或return均可
        else:
            print("请输入正确选项")

def register():
    while True:
        name = input("user:")

        if name=="":
            main()

        password=getpass.getpass()
        password1=getpass.getpass("again：")
        if password!=password1:
            print("两次输入不一致")
            continue
        if " " in name or ' ' in password:
            print('用户名密码不能有空格')
            continue

        msg="R %s %s "%(name,password)
        sockfd.send(msg.encode())
        data= sockfd.recv(1024).decode()

        if data=="ok":
            print("注册成功")
            login_next(name)
        else:
            print("注册失败")
        return ####返回if cmd == "1":

def login():
    name = input("user:")
    password = getpass.getpass()
    msg="L %s %s "%(name,password)
    sockfd.send(msg.encode())
    data=sockfd.recv(1024).decode()
    if data=='ok':
        print("登录成功")
        login_next(name)
    else:
        print("登录失败")

def main():
    while True:
        print("""
        ==============welcome================
            1.注册    2.登录    3.退出
        =====================================
        """)
        cmd = input("请输入命令：")
        if cmd == "1":
            register()
        elif cmd == "2":
            login()
        elif cmd == "3":
            sockfd.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项")

if __name__ == '__main__':
    main()