'''
##########demo.py
"""
二级界面
"""
def fun():
    while 1:
        print("二级界面")
        cmd = input("二级命令")
        if cmd == "查单词":
            pass
        elif cmd == "查历史记录":
            pass
        elif cmd == "注销":
            break

while 1:
    print("一级界面")
    cmd=input("一级命令")
    if cmd=="登录":
        fun()
    elif cmd=="注册":
        fun()
    elif cmd=="退出":
        break
'''

'''
import getpass
password=getpass.getpass()# 功能：隐藏输入内容
print(password)
import hashlib
hash=hashlib.md5()
hash.update(password.encode())
pwd=hash.hexdigest()
print(pwd)
hash=hashlib.md5("$$$a".encode())
hash.update(password.encode())
pwd=hash.hexdigest()
print(pwd)

'''

import pymysql
###############read_db.py
def hist(name):
    db=pymysql.connect(host='localhost',port=3306,user='root',
                       password='123456',database='dict',charset='utf8')
    cur=db.cursor()
    # sql="select * from hist where name='star';"
    sql="select * from hist where name='%s';"%name
    cur.execute(sql)  ##执行正确后，ｃｕｒ调用函数获取结果
    many_row=cur.fetchmany(2)##不会重复获取one_row
    print(many_row)
    print(many_row[0][3])
    # print(many_row[0][3].encode())###报错AttributeError: 'datetime.datetime' object has no attribute 'encode'

    msg="%s"%many_row[0][3]
    print(msg.encode())
    print(("%s"%many_row[0][3]).encode())

    # print("%s"%many_row[0][3].encode())###报错AttributeError: 'datetime.datetime' object has no attribute 'encode'

    cur.close()
    db.close()
# hist()

name='star'
hist(name)


# xj="'%s'"%name
# print(xj)


# x=('a','d','d')
# print(" ".join(x))
# print(x.split(" "))

# name='嘻嘻'
# sl=("%s没有历史记录"%name).encode()
# print(sl)