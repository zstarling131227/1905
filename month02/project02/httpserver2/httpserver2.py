#############htttpserver.py
# (看/home/tarena/1905/month02/code/code3/day06)
"""
httpserver v2.0
env: python3.6
io多路复用 和 http训练
"""
from socket import *
from select import *

class HTTPServer:
    def __init__(self, host='0.0.0.0', port=1234, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        self.rlist=[]
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.address)

    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)

        ##设置关注列表
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    # print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self,connfd):
        request=connfd.recv(4096)####request是字节串
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line=request.splitlines()[0]#######将字节串按行切割
        # print(request_line)
        info=request_line.decode().split(' ')[1]
        # print(info)
        print(connfd.getpeername(),':',info)#########获取连接的客户端的地址.网页输入服务端地址'127.0.0.1/内容'检验代码结果

        if info =='/'  or info[-5:] =='.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)

    def get_html(self,connfd,info):
        if info=='/':
            filename=self.dir+"/index.html"
        else:
            filename=self.dir +info
        try:
            fd=open(filename)
        except Exception:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry....</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"###头
            response += "Content-Type:text/html\r\n"###行
            response += "\r\n"###体
            response += fd.read()
        finally:
            connfd.send(response.encode())


    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"  ###头
        response += "Content-Type:text/html\r\n"  ###行
        response += "\r\n"  ###体
        response += "waiting for httpserver 3.0"
        connfd.send(response.encode())

if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 1234
    DIR = './static'
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.serve_forever()
