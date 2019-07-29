##相当于服务端
"""
webframe.py  模拟后端应用工作流程

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json
from settings import *
from select import select
from urls import *
# 应用类 ：处理网站中某一方面的请求
class Application:
    def __init__(self):
        self.sockfd = socket()
        self.rlist=[]
        self.wlist = []
        self.xlist = []
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind((frame_ip,frame_port))

    def start(self):
        self.sockfd.listen(5)
        print("Start app listen %s"%frame_port)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    def handle(self,connfd):
        request=connfd.recv(1024).decode()
        request1=json.loads(request)
        '''
        代码测试:
        print(request1)
        """
        request1的输出结果为：
        {'method': 'GET', 'INFO': '/abc'}
        {'method': 'GET', 'INFO': '/favicon.ico'}
        {'method': 'GET', 'INFO': '/'}
        """
        d={'status': '200', 'data': '**************'}
        connfd.send(json.dumps(d).encode())
        '''
        if request1['method']=='GET':
            if request1['INFO']=='/' or request1['INFO'][-5:]=='.html':
                response=self.get_html(request1['INFO'])
            else:
                # response={'status': '200', 'data': '**************'}
                response=self.get_data(request1['INFO'])

        elif request1['method']=='POST':
            pass
        ##response的形式是 {'status': '200', 'data': '**************'}
        response=json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    def get_html(self,info):
        if info=='/':###想获取主页
            filename=DIR+"/index.html"
        else:
            filename=DIR +info
        try:
            fd=open(filename)
        except Exception:
            fd = open(DIR + '/404.html')
            return {'status': '404', 'data': fd.read()}
        else:
            return {'status': '200', 'data':fd.read()}

    def get_data(self,info):
        for url,func in urls:
            if url==info:
                return {'status': '200', 'data':func()}
        return {'status': '404', 'data':'sorry...'}

app=Application()
app.start()

"""
127.0.0.1:1234 进入主页index.html

数据处理
127.0.0.1:1234/time 进入数据处理，显示当前时间
127.0.0.1:1234/hello 进入数据处理，打印hello world
127.0.0.1:1234/bye 进入数据处理，打印goodbye
/后跟任意字符，不以.html结尾
127.0.0.1:1234/（str） 进入数据处理，显示sorry...
例如：
127.0.0.1:1234/abc 进入数据处理，显示sorry...

网页处理
包含在.static文件夹中的网页
127.0.0.1:1234/index.html 进入index.html主页
127.0.0.1:1234/net.html 进入net.html主页
127.0.0.1:1234/404.html 进入404.html主页
……
不包含在.static文件夹中的网页
127.0.0.1:1234/405.html 进入404.html主页

"""