'''
作业　：　1. 将文件操作总结
　　　　　2. 总结面试要求题目的回答（看文件操作总结）
　　　　　3. 将服务端流程函数熟练
'''
import socket
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)
sockfd.bind(('0.0.0.0',1234))
sockfd.listen(6)
print("waiting for connecting...")
connfd,addr=sockfd.accept()
print("Connect from",addr)
data=connfd.recv(1024)
n=connfd.send(b'wangbadan')
connfd.close()
sockfd.close()