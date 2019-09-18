from random import randint
from multiprocessing import Process
from multiprocessing import Pool
from time import sleep,ctime
import os,sys,time,random,threading
from multiprocessing import Pipe
from multiprocessing import Queue
from multiprocessing import Value
# from multiprocessing import Array
from multiprocessing import Semaphore
from threading import Thread,Event,Lock

############pipe.py
# #fd1,fd2=Pipe(False)#False是单向管道
# fd1,fd2=Pipe()
# def app1():
#     print("启动应用1,请登录")
#     print("请求app2,授权")
#     fd1.send("app1 请求登录")
#     data=fd1.recv()
#     if data:
#         print("登录成功：",data)
#
# def app2():
#     data=fd2.recv()###阻塞等待读取管道内容
#     print(data)
#     fd2.send(("wangbadan",'123'))
# p1=Process(target=app1)
# p2=Process(target=app2)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

############queue_0.py
##创建消息队列
# q1=Queue(maxsize=3)
# q=Queue(10)###最大长度
# def handle():
#     for i in range(6):
#         x=randint(1,33)###randint包含３３
#         q.put(x)###不断入队
#     q.put(randint(1,16))
#
# def request():
#     l=[]
#     for i in range(6):
#         l.append(q.get())
#     l.sort()
#     l.append(q.get())
#     print(l)
# p1=Process(target=handle)
# p2=Process(target=request)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# data="wangbadan"
# q.put(1)
# q.put(2)
# q.put(4)
# q.put(3)
# print(q.full())
# print(q.empty())
# print(q.qsize())
# q.put(data,block=True)
# q.put(data,block=False)
# q.put(data,timeout=3)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.full())
# print(q.empty())
# print(q.qsize())
# q.close()

############value.py
# money=Value('i',5000)
# def man():
#     for i in range(30):
#         time.sleep(0.2)
#         money.value+=random.randint(1,1000)

# def girl():
#     for i in range(30):
#         time.sleep(0.15)
#         money.value-=random.randint(100,900)
#
# p1=Process(target=man)
# p2=Process(target=girl)
# p1.start()
# p2.start()
# p1.join()
# p2.join()
# a=money.value
# print("一个月余额：",money.value)

############array.py
# # shm=Array('i',[1,2,4,5])
# # shm=Array('i',5)##初始值开辟５个整形空间，ｉ表示整形类型，ｆ表示浮点型
# shm=Array('c',b'hello')##ｃ表示字符串
# def fun():
#     for i in shm:
#         print(i)
#     # shm[1]=1000
#     shm[0]=b'H'
# p=Process(target=fun)
# p.start()
# p.join()
# print("===========")
# for i in shm:
#     print(i)
# print(shm.value)####只能打印字节串

############sem.py
# sem=Semaphore(3)
# def handle():
#     sem.acquire()###执行结束消耗一个信号量
#     print("%s 执行任务"%os.getpid())
#     sleep(2)
#     print("%s 执行任务完毕"%os.getpid())
#     sem.release()###执行结束增加一个信号量
#
# for i in range(10):
#     p1=Process(target=handle)
#     p1.start()

############thread1.py
# a=1
# def fun():
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(),"wangbadan")
#         global a
#         print("a= ",a)
#         a=10000
# # th=Thread(target=fun)
# th=threading.Thread(target=fun)
# th.start()
# for i in range(4):
#     sleep(1)
#     print(os.getpid(),"wangba")
# th.join()
# print("a:",a)

##########thread2.py
# def fun(sec,name):
#     print("线程函数参数")
#     sleep(sec)
#     print("%s执行完毕"%name)
# jobs=[]
# for i in range(5):
#     t=Thread(target=fun,args=(2,),kwargs={'name':'T%d'%i})
#     jobs.append(t)
#     t.start()
#     # print(jobs)
#
# for i in jobs:
#     i.join()

##########thread_attr.py
# def fun():
#     sleep(3)
#     print("线程属性测试")
# t = Thread(target=fun,name='tarena')
# t.setDaemon(True)
# t.start()
# t.setName("Tedu")
# print("name:",t.getName())
# print("is_alive:",t.is_alive())
# print("isDaemon:",t.isDaemon())

##########thread_class.py
# class ThreadClass(Thread):
#     def __init__(self,*args,**kwargs):
#         self.attr=args[0]
#         super().__init__()
#     def f1(self):
#         print("step1:")
#     def f2(self):
#         print("step2:")
#     def run(self):
#         self.f1()
#         self.f2()

# t = ThreadClass('abc')
# t.start() # 自动运行run
# t.join()

##########mythread.py
# class MyThread(Thread):
#     def __init__(self,target=None,args=(),kwargs={}):
#         super().__init__() # 此行不许传参
#         self.target=target
#         self.args=args
#         self.kwargs=kwargs
#     def run(self):
#         self.target(*self.args,**self.kwargs)
###########################################
# def player(sec,song):
#     for i in range(3):
#         print("Playing %s : %s"%(song,ctime()))
#         sleep(sec)
#
# t = MyThread(target=player,args=(3,),
#              kwargs={'song':'凉凉'})
# t.start()
# t.join()

##########thread_event.py
# s=None
# e=Event()
# def 杨子荣():
#     print("杨子荣前来拜山头")
#     global s
#     s="天王盖地虎"
#     e.set()
# t=Thread(target=杨子荣)
# t.start()
# print("说对口令就是自己人")
# e.wait()
# if s=="天王盖地虎":
#     print("宝塔镇河妖")
#     print('确认过眼神你就是对的人')
# else:
#     print("打死他．．．．")

##########thread_lock.py
# a=b=0
# lock=Lock()
# def value():
#     while 1:
#         lock.acquire()
#         if a!=b:
#             print("a=%d b=%d"%(a,b))
#         lock.release()
# t=Thread(target=value)
# t.start()
# while 1:
#     with lock:####上锁
#         a+=1
#         b+=1
            ###自动解锁
# t.join()

############dead_lock.py
"""
class Account:
    def __init__(self,_id,balance,lock):
        self.id=_id
        self.balance=balance
        self.lock=lock

    def withdraw(self,amount):
        self.balance-=amount

    def deposit(self,amount):
        self.balance+=amount

    def get_balance(self):
        return self.balance

Wangbadan=Account("wangbadan",5000,Lock())
Wang=Account("wang",9000,Lock())

def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount)
        # sleep(0.5)##########产生死锁
        if to.lock.acquire():
            to.deposit(amount)
            to.lock.release()
        from_.lock.release()
    print("%s给%s转账%d完成"%(from_.id,to.id,amount))
# transfer(Wangbadan,Wang,4000)
t1=Thread(target=transfer,args=(Wangbadan,Wang,2000))
t2=Thread(target=transfer,args=(Wang,Wangbadan,2000))
t1.start()
t2.start()
t1.join()
t2.join()
"""