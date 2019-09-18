#####socket
#####ifconfig
#####ping
#####os
#####socket.socket

##########with.py
"""
with.py
使用ｗｉｔｈ语句打开文件
"""
# with open('exercise02.py') as f:
#     data=f.read()
#     print(data)

###########buffer.py
"""
buffer.py 文件读写缓冲机制演示

缓冲刷新条件：
1. 缓冲区满了
2. 行缓冲换行时会自动刷新
3. 程序运行结束或者文件close关闭
4. 调用flush()函数
"""
# f=open('test','w',1)
# while 1:
#     data=input("..")
#     if not data:
#         break
#     f.write(data)
#     f.flush()
# f.close()

# f.read(data)

###########seek.py
"""
seek.py  文件偏移量示例

注意: 1. 每次open 打开文件文件偏移量都在开头　
　　　2. 已ａ方式打开时文件偏移量在结尾
　　　3. 读写操作共用一个文件偏移的
"""
# f=open("test",'rb+')
# data=f.read(10)
# print("文件偏移量：",f.tell())
# f.seek(10,2)
# f.write(b'&&&&&')
# f.close()

###########hold.py
"""
空洞文件
"""
# f = open('test','wb')
# f.write(b'start')
# f.seek(1024*1024,2) #　从结尾向后移动１k
# f.write(b'end')
# f.close()

######tcp_server.py
"""
tcp_server.py  tcp套接字服务端流程
重点代码

注意：　功能性代码，注重流程和函数使用
"""
#######服务端代码
import  socket
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.bind(("127.0.0.1",1234))
sockfd.listen(5)
while 1:
    print("waiting for connect...")
    try:
        connfd,addr=sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("服务器退出")
        break
    except Exception as e:
        print(e)
        continue
    while 1:
        data=connfd.recv(1024)
        if not data:
            break
        print("收到：",data.decode())
        print("收到：",data)
        n=connfd.send(b'Thanks')
        print("发送%d个字节"%n)
    connfd.close()
sockfd.close()
###########在终端输入（tarena@tarena:~$ telnet 127.0.0.1 1234）
