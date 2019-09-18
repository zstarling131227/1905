import pymysql
import re
'''
###########mysql.py
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()
sql='insert into class_1 values(7,"吱吱",17,"m",76.5,"2019-8-8");'
####封号可加可不加
cur.execute(sql)
db.commit() ###只有写操作需要提交。可以多次写操作一同提交。
cur.close()
db.close()
'''

'''
###############read_db.py
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()
# sql="select * from class_1 where gender='w';"
sql="select name,age from class_1 where gender='w';"
cur.execute(sql)  ##执行正确后，ｃｕｒ调用函数获取结果

# one_row=cur.fetchone()
# print(one_row)
# print(one_row[5])

# many_row=cur.fetchmany(2)##不会重复获取one_row
# print(many_row)

all_row=cur.fetchall()
print(all_row)
cur.close()
db.close()
'''

'''
###############write_db.py
# (update...set,delete...from,insert into..)
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()
try:
    # name=input("name:")
    # age=int(input("age:"))
    # age=input("age:")
    # score=float(input("score:"))
    # score=input("score:")
    ###将变量插入到ｓｑｌ语句合成最终操作语句
    # sql="insert into class_1 (name,age,score) values (%s,%s,%s)"%(name,age,score)###报错
    # sql="insert into class_1 (name,age,score) values ('%s','%s','%s')"%(name,age,score)
    # sql="insert into class_1 (name,age,score) values ('%s',%d,%f)"%(name,age,score)
    # cur.execute(sql)

    ###预留列表传值
    # sql="insert into class_1 (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name,age,score])  ##任意类型均可以,[name,age,score]是复制给values后的值的。

    # sql="update class_1 set gender='m' where id='8';"
    # cur.execute(sql)

    # sql="delete from class_1 where age<16;"
    # cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback()  ###退回到conmit执行之前的数据库状态。
    print(e)
cur.close()
db.close()
'''

'''
##########练习
"""
mysql> create database dict charset(utf8);
创建数据库　ｄｉｃｔ
mysql> create table wordss(id int primary key auto_increment, word char(32),mean text);
创建数据表　ｗｏｒｄs
将单词存入words词表　超过19500即可
"""
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='dict',charset='utf8')
cur=db.cursor()
f=open('dict.txt')
###自己写
# for i in f:
#     sql='insert into words (word,explain1) values(%s,%s);'
#     cur.execute(sql,[i.split(" ")[0]," ".join(i[1:]).strip()])
#     db.commit()

##老师讲
sql='insert into wordss (word,mean) values(%s,%s);'
for i in f:
    tup=re.findall(r"(\S+)\s+(.*)",i)[0]
    # print(tup)
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        db.rollback()

####普通写法
# data=f.readline()
# tmp=data.split(" ")
# print(tmp)
# word=tmp[0]
# mean=" ".join(tmp[1:]).strip()
# print(word)
# print(mean)

f.close()
cur.close()
db.close()
'''

'''
#############save_image.py
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()
##存储图片
# with open('img.jpg','rb') as f:
# with open('img1.jpg','rb') as f:
#     data=f.read()
# try:
#     # sql="update class_1 set image=%s where name='丫丫';"
#     sql="update class_1 set image=%s where name='yaoyue';"
#     cur.execute(sql,[data])
#     db.commit()  ###只有写操作需要提交。可以多次写操作一同提交。
# except Exception as e:
#     db.rollback()
#     print(e)
#获取图片
# sql="select image from class_1 where name='丫丫'"
sql="select image from class_1 where name='yaoyue'"
cur.execute(sql)
data=cur.fetchone()
with open("view1.jpg","wb") as f:
    f.write(data[0])

cur.close()
db.close()
'''

"""
编写一个程序模拟注册和登录的过程

   * 创建一个user表 包含 用户名和密码字段
     create table user (id int primary key auto_increment,name varchar(32) not null,passwd varchar(32) not null);

   * 应用程序中模拟注册和登录功能

     注册则输入用户名密码将用户名密码存入到数据库
     （用户名不能重复）

     登录则进行数据库比对，如果有该用户则打印登录成功
     否则让重新输入

"""

'''
###########login.py
"""
mysql> use stu;
mysql> create table user(id int primary key auto_increment,name varchar(32) not null,password1 int not null);
"""
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()
while True:
    choose=input("注册输入1，登录输入2")
    if choose=='1':
        name = input("name:")
        password = input("password:")
        sql = "select * from  user where name ='%s'" % name
        cur.execute(sql)
        result = cur.fetchone()
        if result:
            print("用户名已存在")
        else:
            try:
                sql = 'insert into user (name,password1) values(%s,%s);'
                cur.execute(sql, [name, password])
                db.commit()
                print("注册成功")
            except:
                db.rollback()
    elif choose=="2":
        name = input("name:")
        password =int(input("password:"))
        sql="select * from user where name ='%s' and password1=%d"%(name,password)
        cur.execute(sql)
        result=cur.fetchone()
        if result:
            print("登录成功")
        else:
            print("密码错误")
    else:
        print("臣妾做不到啊")
cur.close()
db.close()
'''

'''
###########login.py(alt+ctrl+m)快捷键定义函数
"""
mysql> use stu;
mysql> create table user(id int primary key auto_increment,name varchar(32) not null,password1 int not null);
"""
db=pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='stu',charset='utf8')
cur=db.cursor()

def register():
    global name, password, sql, result
    name = input("name:")
    password = input("password:")
    sql = "select * from  user where name ='%s'" % name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        print("用户名已存在")
    else:
        try:
            sql = 'insert into user (name,password1) values(%s,%s);'
            cur.execute(sql, [name, password])
            db.commit()
            print("注册成功")
        except:
            db.rollback()

def log_in():
    global name, password, sql, result
    name = input("name:")
    password = int(input("password:"))
    sql = "select * from user where name ='%s' and password1=%d" % (name, password)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        print("登录成功")
    else:
        print("密码错误")

while True:
    choose=input("注册输入1，登录输入2")
    if choose=='1':
        register()
    elif choose=="2":
        log_in()
    else:
        print("臣妾做不到啊")
cur.close()
db.close()
'''

'''
#################老师讲
import  pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')

# 获取游标 （操作数据库，执行sql语句）
cur = db.cursor()

#　注册
def register():
    name = input("用户名:")
    passwd = input("密　码:")
    #判断用户名是否重复
    sql="select * from user where name='%s'"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql="insert into user (name,passwd) \
        values (%s,%s)"
        cur.execute(sql,[name,passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False

def login():
    name = input("用户名:")
    passwd = input("密　码:")
    sql = "select * from user \
    where name='%s' and passwd='%s'"%(name,passwd)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True


while True:
    print("""
             ===============
             1.注册　　2.登录
             ===============
    """)
    cmd = input("输入命令：")
    if cmd ==  '1':
        #　执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")

    elif cmd == '2':
        #　执行登录
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("我也做不到啊")

# 关闭数据库
cur.close()
db.close()
'''