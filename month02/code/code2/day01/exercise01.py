###复制文件(看day02的copy_file.py)
"""
作业: 1. 熟悉文件的基本操作函数
"""
'''
　　　2. 编写一个文件拷贝程序，从终端输入一个文件，
　　　　　将文件保存在当前目录下

        * 文件类型不确定（可是文本文件，可能是二进制文件）
'''
####自己写
# f=open("test",'rb')
# g= open('test1','wb')
# for i in f:
#     l=[i]
#     g.writelines(l)

# #####老师讲
# filename=input("请输入文件名：")
# try:
#     fr=open(filename,'rb')
# except FileNotFoundError as e:
#     print(e)
# else:
#     fw=open("copy_filename.jpg",'wb')
#     while 1:
#         data=fr.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     fw.close()
#     fr.close()

#########看day02的write_time.py
'''
     3. 编写一个程序，向一个文件中写入如下内容：
     　　　
     　　1.  2019-1-1  18:18:18
     　　2.  2019-1-1  18:18:19
     　　3.  2019-1-1  18:18:24

        循环每隔１秒写入一次,序号从１排列
        ctrl-c结束程序，下次启动程序
        序号要与之前的衔接
'''
import time
f=open('log.txt','a+')

f.seek(0,0)
n=0
for i in f:
    n+=1

while True:
    time.sleep(1)
    data=('%d. %s\n'%(n,time.ctime()))
    n+=1
    f.writelines(data)
    f.flush()
