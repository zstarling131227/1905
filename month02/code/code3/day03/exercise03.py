###测试进程线程和单进程的执行效率
#########day04.giz
from test import *
from multiprocessing import Process
import time
from threading import Thread

###########single.py
# tm=time.time()
# for i in range(10):
#     count(1,1)
#     # io()
# print("Single cpu:", time.time() - tm)###Single cpu: 7.217524528503418
# # print("Single io:", time.time() - tm)###Single io: 0.004584550857543945

##########muti_process.py
# jobs = []
# tm = time.time()
# for i in range(10):
#     # p=Process(target=count,args=(1,1))
#     p = Process(target=io)
#     p.start()
#
# for i in jobs:
#     i.join()
# # print("Process cpu:", time.time() - tm)###Process cpu: 0.03204965591430664
# print("Process io:", time.time() - tm)####Process io: 0.011832237243652344

##########muti_thread.py
# jobs = []
# tm = time.time()
# for i in range(10):
#     t=Thread(target=count,args=(1,1))
#     # t = Thread(target=io)
#     t.start()
#
# for i in jobs:
#     i.join()
# print("Thread cpu:", time.time() - tm)###Thread cpu: 1.1654632091522217
# # print("Thread io:", time.time() - tm)#####Thread io: 0.015388011932373047

