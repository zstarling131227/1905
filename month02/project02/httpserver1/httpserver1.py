##########httpserver2.py(看/home/tarena/1905/month02/code/code2/day04)
"""
httpserver2 v1.0
基本要求：
１．获取来自浏览器的请求
２．判断如果请求内容是/，将ｉｎｄｅｘ．ＨＴＭＬ返回给客户
３．如果返回的是其他内容则返回４０４
"""
from socket import *

#　客户端(浏览器)处理
def request(connfd):
    # 获取请求将请求内容提取出来
    data=sockfd.recv(4096)
    print(data)
    """
    data的输出结果是：b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1234\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
    """
    if not data:
        return
    request_line=data.decode().split("\n")[0]
    print(request_line)#######运行代码后．去网页运行网址，在控制台才会显示结果
    info=request_line.split(" ")[1]
    print(info)
    # 判断是/ 则返回index.html 不是则返回404
    if info == '/':
        with open("index.html") as f:
            response="HTTP/1.1 200 OK\r\n"
            response+="Content-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry....</h1>"
    connfd.send(response.encode())

#　搭建ｔｃｐ网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)
while True:
    connfd,addr = sockfd.accept()
    request(connfd) #　处理客户端请求