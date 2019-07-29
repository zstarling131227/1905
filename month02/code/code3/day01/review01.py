###终端运行代码
#######ps -aus####查看进程
#######ps -tree

#########fork.py
"""
fork.py fork进程创建演示1
"""
# import os
# from time import sleep
# pid=os.fork()
# if pid<0:
#     print("Creat failed")
# elif pid==0:
#     print("the new process")
# else:
#     print("the old process")
# print("Fork test over")

# #########fork1.py()注意a 的输出
# import os
# print("==========")######仅仅是打印语句
# a=1####赋值语句会开辟变量空间
# pid=os.fork()
# if pid<0:
#     print("Creat failed")
# elif pid==0:
#     print("the new process")
#     print("a=",a)
#     a=1000
# else:
#     print("the old process")
#     # print('a=',a)
# print("Fork test over")


#########get_pid.py
# import os
# pid=os.fork()
# if pid<0:
#     print("Error")
# elif pid==0:
#     print("Child PID",os.getpid())
#     print("Get Parent PID",os.getppid())
# else:
#     print("Get Child PID", pid)
#     print("Parent PID", os.getpid())

#########get_pid.py
"""
获取进程PID号
"""
# import os
# from time import *
# pid=os.fork()
# if pid<0:
#     print("Error")
# elif pid==0:
#     sleep(3)
#     print("Child PID",os.getpid())
#     print("Get Parent PID",os.getppid())
# else:
#     print("Get Child PID", pid)
#     print("Parent PID", os.getpid())
#########在终端运行时，才会显示出结果差异
"""
输出结果：
tarena@tarena:~/1905/month02/code/code3/day01$ python3 review01.py
Get Child PID 28166
Parent PID 28165####生成子进程的父进程(生父）的ｐｉｄ
tarena@tarena:~/1905/month02/code/code3/day01$ Child PID 28166
Get Parent PID 1####父进程消失后，子进程的新的父进程(继父）的ｐｉｄ.
"""

############结束一个进程exit.py
# import os,sys
# # os._exit(0) # 退出进程
# sys.exit("退出") # 退出进程
# print("exit test")

##########zombie.py
"""
模拟僵尸进程产生
"""
# import os,sys
# pid=os.fork()
#
# if pid<0:
#     print("Error")
# elif pid==0:
#     print("Child PID",os.getpid())
#     sys.exit("子进程退出")
# else:
#     while 1:
#         pass
###########结果在终端输入ps -aux查看是否生成子进程Child PID 32447

# ############wait.py(方法１；避免僵尸进程的产生)
# import os,sys
# pid=os.fork()
# if pid<0:
#     print("Error")
# elif pid==0:
#     print("Child PID",os.getpid())
#     # sys.exit("子进程退出")##########输出结果为status: 256
#     sys.exit(2)##########输出结果为status: 512
# else:
#     pid,status=os.wait()
#     print("pid:",pid)
#     print("status:",status)
#     while 1:
#         pass

# ###########child.py(方法２；避免僵尸进程的产生)
# from time import sleep
# import os
# def f1():
#     for i in range(3):
#         sleep(2)
#         print("写代码")
# def f2():
#     for i in range(2):
#         sleep(4)
#         print("测代码")
# pid=os.fork()
# if pid==0:
#     p=os.fork()
#     if p==0:
#         f1()
#     else:
#         os._exit(0)
# else:
#     os.wait()
#     f2()


###########signal_.py(方法３；通过信号处理，避免僵尸进程的产生)
import signal
import os,sys
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    print("Child PID",os.getpid())
    sys.exit("子进程退出")
else:
    while 1:
        pass
###########结果在终端输入ps -aux查看是否生成子进程Child PID 32447
