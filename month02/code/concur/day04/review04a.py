from multiprocessing import Process
from threading import Thread
from socket import *
import os  # 创建子进程
import sys, time
import signal  # 处理僵尸进程

"""
######copy-file.py(看day02中的exercise02.py)
filename='./img.jpg'
size=os.path.getsize(filename)
fr=open(filename,'rb')##fr,放在外面父进程中打开.运行时会有影响.

def top():###上半部分大小为一半
    fw=open("img_top.jpg",'wb')
    n=size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

def bottom():###上半部分大小为0
    fw=open("img_bottom.jpg",'wb')
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1=Process(target=top)
p2=Process(target=bottom)
p1.start()
p2.start()
p1.join()
p2.join()
"""
'''
#########fork_server.py
HOST="0.0.0.0"
PORT=1234
ADDR=(HOST,PORT)

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

sockfd=socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(5)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("listening the port 1234...")

while True:
    try:
        c,addr=sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    pid=os.fork()
    if pid==0:
        sockfd.close()###关闭子进程.对父进程没有影响
        handle(c)
        os._exit(0)#子进程销毁
    #无论父进程还是fork出错都要回去继续处理链接
    else:
        c.close()

    while True:
        p = Process(target=handle)
        p.start()
        p.join()
'''
'''
##########process_server.py
HOST = "0.0.0.0"
PORT = 1234
ADDR = (HOST, PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(5)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listening the port 1234...")

while True:
    try:
        c, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    p = Process(target=handle,args=(c,))
    p.daemon=True#父进程退出,子进程也退出.就是所有服务终止
    p.start()
'''
'''
# ###########thread_server.py
HOST = "0.0.0.0"
PORT = 1234
ADDR = (HOST, PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(5)

print("listening the port 1234...")

while True:
    try:
        c, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle,args=(c,))
    t.setDaemon(True)#父进程退出,子进程也退出.就是所有服务终止
    t.start()
'''

########ftp_server.py
"""
ftp 文件服务器，服务端
env : python3.6
多进程/线程并发 socket
"""
# 定义全局变量
HOST = "0.0.0.0"
PORT = 1234
ADDR = (HOST, PORT)

# 创建文件夹
FTP = "/home/tarena/1905/month02/code/code3/day04/ftp/"


# 创建操作类
class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    # 查看
    def look(self):
        files = os.listdir(FTP)  ##获取文件列表os.listdir(",")#获取文文件夹下的文件目录
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        filelist = ""
        for file in files:
            if file[0] != "." and os.path.isfile(FTP + file):
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    # 下载
    def download(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)  ###防止发送OK与文件内容粘包
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)

    # 上传
    def upload(self, filename):
        if filename in os.listdir(FTP):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b"ok")
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 上传(老师讲)
    def upload1(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b"ok")
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # print(data)
            if not data or data == "Q":
                return  # 线程结束
            elif data == "L":
                self.look()
            elif data[0] == "D":
                filename = data.split(" ")[-1]
                self.download(filename)
            elif data[0] == "U":
                filename = data.split(' ')[-1]
                self.upload(filename)


##搭建网络客户端模型
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("listening the port 1234...")

    while True:
        try:
            c, addr = sockfd.accept()
            print("Connect from:", addr)
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue

        client = FTPServer(c)
        client.setDaemon(True)  # 父进程退出,子进程也退出.就是所有服务终止
        client.start()


if __name__ == "__main__":
    main()
