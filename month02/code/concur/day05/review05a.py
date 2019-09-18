from socket import *
from time import ctime, sleep
import select
from select import *

'''
##########block_io.py
"""
block_io.py
socket 套接字非阻塞示例
"""
f=open('log.txt','a+')

sockfd=socket()
sockfd.bind(('127.0.0.1',1234))
sockfd.listen(5)

sockfd.setblocking(False)
# sockfd.settimeout(3)

while True:
    print("Waiting for connecting...")
    try:
        connfd,addr=sockfd.accept()
    except (BlockingIOError,timeout) as e:
        sleep(3)
        f.write("%s : %s\n"%(ctime(),e))
        f.flush()
    else:
        print("Connect from",addr)
        data=connfd.recv(1024).decode()
        print(data)
'''

'''
##########select_test.py
"""
select 函数示例
"""
s=socket()
s.bind(("0.0.0.0",1234))
s.listen(3)
print("监控io")
##终端输入'talnet 127.0.0.1 1234 '测试
# rs,ws,xs=select([s],[],[])########陷入阻塞
# rs,ws,xs=select([],[],[s])
# rs,ws,xs=select([s],[],[],3)
f=open("log.txt","r+")
rs,ws,xs=select([s],[f],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)
'''

'''
##########select_server.py
"""
select tcp服务
重点代码

思路分析：
1. 将关注的IO放入到监控列表
2. 当IO就绪时会通过select返回
3. 遍历返回值列表，得知哪个IO就绪进行处理
"""
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 1234))
sockfd.listen(5)

##设置关注列表
rlist = [sockfd]
wlist = []
xlist = []
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is sockfd:
            c, addr = r.accept()
            print("Connect from", addr)
            """        
            ##只能执行一个客户端,不能用多个
            while True:
                data=c.recv()
                print(data)
                c.send(b'ok')
            """
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b'ok')
            wlist.append(r)

    for w in ws:
        w.send(b'ok')
        wlist.remove(w)

    for x in xs:
        pass
'''

'''
##############poll_server.py
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 1234))
sockfd.listen(5)

p=poll()

fdmap={sockfd.fileno():sockfd}

p.register(sockfd,POLLIN|POLLERR)

while True:
    events=p.poll()
    # print(events)########在pycharm运行,poll处会阻塞(等待客户端链接),在终端运行telnet 127.0.0.1 1234会输出结果[(3, 1)]
    for fd,event in events:
        # print("fileno:",fd)
        # print("event:",event)
        if fd==sockfd.fileno():
            c,addr=fdmap[fd].accept()
            print('Connect from',addr)
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()]=c####维护字典
        # else:
        elif event & POLLIN:####判断是否为pollin就绪
            data=fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'ok')
'''

'''
##########epoll_server.py
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 1234))
sockfd.listen(5)

ep=epoll()

fdmap={sockfd.fileno():sockfd}

ep.register(sockfd,EPOLLIN|EPOLLERR)

while True:
    events=ep.poll()
    # print(events)########在pycharm运行,poll处会阻塞(等待客户端链接),在终端运行telnet 127.0.0.1 1234会输出结果[(3, 1)]
    for fd,event in events:
        # print("fileno:",fd)
        # print("event:",event)
        if fd==sockfd.fileno():
            c,addr=fdmap[fd].accept()
            print('Connect from',addr)
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()]=c####维护字典
        # else:
        elif event & EPOLLIN:####判断是否为pollin就绪
            data=fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'ok')
'''

###############yeild.py

def fun():
    print("start")
    yield
    print("end")
g=fun()
print(g.__next__())
print(g.__next__())

