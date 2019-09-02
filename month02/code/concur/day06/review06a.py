'''
############ASYNC_test.py
import asyncio
async def fun1():
    print("START1")
    await asyncio.sleep(2)
    print("end1")

async def fun2():
    print("START2")
    await asyncio.sleep(3)
    print("end2")
con1=fun1()
con2=fun2()
tasks=[asyncio.ensure_future(con1),asyncio.ensure_future(con2)]
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
'''

'''
############greenlet_0.py
import greenlet
def fun1():
    print("wangbadan")
    gr2.switch()
    print("wangba")
    gr2.switch()
def fun2():
    print("wan")
    gr1.switch()
    print("wang")
gr1=greenlet.greenlet(fun1)
gr2=greenlet.greenlet(fun2)
gr1.switch()
'''

'''
############gevent_test.py
"""
协成模块 示例
"""
# import gevent
# def foo(a,b):
#     print("Runing foo.........",a,b)
#     print("foo again..")

# gev1=gevent.spawn(foo,1,2)
# ###以下两种方法都不可以阻塞
# # sleep(5)
# # while 1:
# #     pass
# gevent.sleep(5)

#######示例2
# import gevent
# from time import sleep
# def foo(a,b):
#     print("Runing foo.........",a,b)
#     print("foo again..")
#
# def bar(a,b):
#     print("Runing bar.........",a,b)
#     print("bar again..")
#
# gev1=gevent.spawn(foo,1,2)
# gev2=gevent.spawn(bar,1,2)
# gevent.joinall([gev1,gev2])

#########示例3
# import gevent
# from time import sleep
# def foo(a,b):
#     print("Runing foo.........",a,b)
#     gevent.sleep(4)
#     print("foo again..")
#
# def bar(a,b):
#     print("Runing bar.........",a,b)
#     gevent.sleep(3)
#     print("bar again..")

# gev1=gevent.spawn(foo,1,2)
# gev2=gevent.spawn(bar,1,2)
# gevent.joinall([gev1,gev2])

##########示例4
# import gevent
# from gevent import monkey
# monkey.patch_time()
# # monkey.patch_socket()
# # monkey.patch_all(bool=True)
# def foo(a,b):
#     print("Runing foo.........",a,b)
#     gevent.sleep(4)
#     print("foo again..")
# 
# def bar(a,b):
#     print("Runing bar.........",a,b)
#     gevent.sleep(3)
#     print("bar again..")

# gev1=gevent.spawn(foo,1,2)
# gev2=gevent.spawn(bar,1,2)
# gevent.joinall([gev1,gev2])
'''

'''
############gevent_server.py
"""
gevent server 基于协成的TCP并发

思路: 1.将每个客户端的处理设置为协成函数
     2. 让socket模块下的阻塞可以触发协程跳转
"""
import gevent
from gevent import monkey
monkey.patch_socket()
from  socket import *
def handle(c):
    while 1:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'ok')

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",1234))
s.listen(3)

while 1:
    c,addr=s.accept()
    print("Connect from",addr)
    # handle(c)
    gevent.spawn(handle(c))###遇到gevent类型的阻塞时才会执行，并不会立即执行。
'''


