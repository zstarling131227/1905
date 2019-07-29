##问题是出现网页加载只允许一个，修改看httpserver3a.py
##对应webframe.py

##先运行webframe.py,再运行httpserver3.py
##在浏览器运行，输入127.0.0.1:1234/abc。网页显示d = {'status': '200', 'data': 'xxxxxxxx'}中的xxxxxxxx
##运行两个网页时，只有一个会加载出xxxxxxxx。
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

class HTTPServer:

    def __init__(self):
        self.address = ADDR
        self.create_socket()
        self.connect_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)###自己定义调试

    def connect_socket(self):
        self.connect_sockfd=socket()
        frame_addr=(frame_ip,frame_port)
        try:
            self.connect_sockfd.connect(frame_addr)
        except Exception as e:
            print(e)
            sys.exit()

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
        # print(request)##测试
        """
        终端输入127.0.0.1:1234
        request的输出结果:
        Connect from ('127.0.0.1', 42284)
        GET / HTTP/1.1
        Host: 127.0.0.1:1234
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        
        终端输入127.0.0.1:1234/abc
        request的输出结果:
        Connect from ('127.0.0.1', 42320)
        GET /abc HTTP/1.1
        Host: 127.0.0.1:1234
        Connection: keep-alive
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        """
        # pattern=r'([A-Z]+)\s+(/\S*)' ##([A-Z]+)请求类型，(/\S)请求内容
        pattern=r'(?P<method>[A-Z]+)\s+(?P<INFO>/\S*)' ##捕获组
        try:
            # env=re.match(pattern,request)####测试
            """
            env输出结果：
            <_sre.SRE_Match object; span=(0, 8), match='GET /abc'>
            """
            env=re.match(pattern,request).groupdict()##返回捕获组组名和内容
            """
            env输出结果：
            {'method': 'GET', 'INFO': '/abc'}
            """
        except:
            connfd.close()
            return
        else:
            # print(env)##测试
            data=json.dumps(env)
            self.connect_sockfd.send(data.encode())
            data=self.connect_sockfd.recv(4096*100).decode()
            # print(json.loads(data))##测试
            self.response(connfd,json.loads(data))

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
    # DIR = './static'
    httpd = HTTPServer()
    httpd.serve_forever()