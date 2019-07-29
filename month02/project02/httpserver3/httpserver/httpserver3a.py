"""
##对应webframe1.py
##先运行webframe1.py,再运行httpserver3a.py
’‘’在浏览器运行，输入127.0.0.1:1234/abc。网页显示d = {'status': '200', 'data':
'**************'}中的**************。运行两个网页时，都会加载出**************。
若是代码修改，可通过HTTPServer多网页加载.rar。老师版的验证‘’‘
"""
"""
httpserver 的部分主程序

获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
from socket import *
import sys,re,json
from threading import Thread
from config import *
from select import *

ADDR=(HOST,PORT)

###和webframe通信的函数
def connect_frame(env):
    s=socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
    data = json.dumps(env)
    s.send(data.encode())
    data = s.recv(4096 * 100).decode()
    return json.loads(data)

class HTTPServer:

    def __init__(self):
        self.address = ADDR
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)###自己定义调试

    def bind(self):
        self.sockfd.bind(self.address)
        self.ip=self.address[0]
        self.port=self.address[1]

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)

        while True:
            connfd,addr=self.sockfd.accept()
            print("Connect from", addr)
            client=Thread(target=self.handle,args=(connfd,))
            client.setDaemon(True)
            client.start()

    def handle(self,connfd):
        request=connfd.recv(4096).decode()
        pattern=r'(?P<method>[A-Z]+)\s+(?P<INFO>/\S*)' ##捕获组
        try:
            env=re.match(pattern,request).groupdict()##返回捕获组组名和内容
        except:
            connfd.close()
            return
        else:
            data=connect_frame(env)
            if data:
                self.response(connfd,data)

    def response(self,connfd,data):
         ##data表示：{'status':'200','data':'xxxxxxxx'}
        if data["status"]=="200":
            responseHeaders = "HTTP/1.1 200 OK\r\n"  ###头
            responseHeaders += "Content-Type:text/html\r\n"  ###行
            responseHeaders += "\r\n"  ###体
            responseBody = data['data']
        elif data["status"]=="404":
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data["status"]=="500":
            pass
        response_data=responseHeaders+responseBody
        connfd.send(response_data.encode())



if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()