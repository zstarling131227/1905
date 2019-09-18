from socket import *
import os, sys, time

'''
#########tcp_client.py
sockfd = socket()
server_addr = ('127.0.0.1',1234)
sockfd.connect(server_addr)
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("Server:",data.decode())
sockfd.close()
'''

#########ftp_client.py
"""
ftp 文件服务，客户端
"""
# 定义全局变量
ADDR = ('127.0.0.1', 1234)


class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    # 查看
    def look(self):
        self.sockfd.send(b'L')
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    # 下载
    def download(self, filename):
        self.sockfd.send(('D ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            f = open(filename, 'wb')
            while 1:
                data = self.sockfd.recv(4096)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    # 上传
    def upload(self, filename):
        self.sockfd.send(('U ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            try:
                f = open(filename, 'rb')
            except Exception:
                print("文件不存在")
                return
            while True:
                data = f.read()
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
        else:
            print(data)

    # 上传(老师讲)
    def upload1(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print("文件不存在")
            return
        filename = filename.split('/')[-1]
        self.sockfd.send(('U ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            while True:
                data = f.read()
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

    # 退出
    def quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")


def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPClient(sockfd)

    while True:
        print("\n ===========命令选项 ==========")
        print("***********  list   **********")
        print("****  download filename   ****")
        print("******* upload filename  *****")
        print("***********  quit   **********")
        print("==============================")
        cmd = input("输入命令:")
        # sockfd.send(cmd.encode())#####测试是否从创键成功
        if cmd.strip() == 'list':
            ftp.look()
        elif cmd.strip() == 'quit':
            ftp.quit()
        elif cmd[:8] == 'download':
            filename = cmd.strip().split(" ")[-1]
            ftp.download(filename)
        elif cmd[:6] == 'upload':
            filename = cmd.strip().split(" ")[-1]
            ftp.upload(filename)
        else:
            print("请输入正确命令")


if __name__ == "__main__":
    main()
