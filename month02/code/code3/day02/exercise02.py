'''作业： 1. 将聊天室代码梳理一下
      2. 熟练multiprocessing模块创建进程
      3. 创建两个进程，分别复制一个文件的上下半部分
      将复制内容放到两个新的文件中，按字节分文件
'''
from multiprocessing import Process
import os
filename='./img.jpg'
size=os.path.getsize(filename)
###上下半部分大小为一半,可以通过终端ls查看大小
def top():
    fr=open(filename,'rb')
    fw=open("img_top.jpg",'wb')
    n=size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

def bottom():######下半部分图片看不到,是因为后半部分图片打开时没有识别图片的标志
    fr=open(filename,'rb')
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