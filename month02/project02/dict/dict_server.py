"""
dict 服务端

功能：业务逻辑处理
模型：多进程 TCP并发
封装：函数
"""
from mysql import Database
from socket import *
from multiprocessing import Process
import socket,signal,sys,time
HOST="0.0.0.0"
PORT=1234
ADDR=(HOST,PORT)
db=Database(database='dict')

def register(c,data):
    tmp = data.split(" ")
    name = tmp[1]
    password = tmp[2]
    result=db.register(name,password)
    if result:
        c.send(b"ok")
    else:
        c.send(b"fail")

def login(c,data):
    tmp=data.split(" ")
    name = tmp[1]
    password=tmp[2]
    result=db.login(name,password)
    if result:
        c.send(b"ok")
    else:
        c.send(b"fail")

def query(c,data):
    tmp=data.split(" ")
    name = tmp[1]
    word=tmp[2]

    db.insert_hist(name,word)

    mean=db.query1(word)

    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg="%s:%s"%(word,mean)
        c.send(msg.encode())

def do_hist(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    history=db.hist(name)
    print(history)
    if not history:
        # c.send(b"failed")
        c.send(("%s没有历史记录"%name).encode())
        # c.send("%s没有历史记录"%name.encode())####报错AttributeError: 'datetime.datetime' object has no attribute 'encode'

        return ###注意退出时要用return

    c.send(b'ok')
    ###发送问题
    for i in history:
        ###时间问题
        msg="%s %-16s %s" %i
        # print(msg)（看demo.py）
        # print(msg.encode())
        time.sleep(0.1) ########没有堵塞会造成粘包
        c.send(msg.encode())
        # c.send(msg.encode() + b'\n')
    time.sleep(0.1) ########没有堵塞会造成粘包
    c.send(b'##')

def do_hist1(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    history=db.hist(name)
    if not history:
        c.send(("%s没有历史记录"%name).encode())
        return
    else:
        for i in history:
            msg="%s %-16s %s"%i
            time.sleep(0.1)
            c.send(msg.encode())
        time.sleep(0.1)
        c.send(b'##')

def request(c):
    db.create_cursor()
    while True:
        data=c.recv(1024).decode()
        print(c.getpeername(),":",data)
        if not data or data[0]== "E":
            sys.exit()
        elif data[0]=="R":
            register(c,data)
        elif data[0] == "L":
            login(c,data)
        elif data[0] == "Q":
            query(c,data)
        elif data[0] == 'H':
            do_hist(c,data)

def main():
    sockfd = socket.socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(4)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    print("Listen the port 1234")
    while True:
        try:
            c,addr=sockfd.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sockfd.close()
            db.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)
            continue
        p=Process(target=request,args=(c,))
        p.daemon=True
        p.start()


if __name__ == '__main__':
    main()