#######chat_client.py
from socket import *
import os, sys

ADDR = ("127.0.0.1", 1234)

def send_msg(sockfd, name):
    while True:
        try:
            text = input("发言：")
        except KeyboardInterrupt:
            text = "quit"
        if text.strip() == "quit":
            msg = "Q " + name
            sockfd.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        sockfd.sendto(msg.encode(), ADDR)


def recv_msg(sockfd):
    while True:
        try:
            data, addr = sockfd.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode()+'\n发言：',end=" ")


def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("name:")
        msg = "L " + name
        sockfd.sendto(msg.encode(), ADDR)
        data, addr = sockfd.recvfrom(128)
        if data.decode() == "ok":
            print("进入聊天室")
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(sockfd, name)
    else:
        recv_msg(sockfd)


main()
