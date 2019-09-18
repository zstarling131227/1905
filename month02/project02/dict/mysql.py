"""
数据库操作模块
思路：
将数据库操作封装一个类，将dict_server需要的数据库操作
功能分别写成方法，在dict_server中实例化对象，需要什么
方法直接调用

"""
import pymysql
import hashlib

SALT="#&aid_#"

class Database:
    def __init__(self,host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = None,
                     charset = 'utf8'):
        self.host=host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.connect_database()
    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user= self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    def close(self):
        self.db.close()

    def create_cursor(self):
        self.cur=self.db.cursor()

    def register(self,name,password):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False

        # hash = hashlib.md5("name + SALT".encode())
        hash = hashlib.md5((name + SALT).encode())
        hash.update(password.encode())
        password= hash.hexdigest()

        sql = "insert into user (name,password) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, password])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False


    def login(self,name,password):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(password.encode())
        password = hash.hexdigest()

        sql = "select * from user where name='%s' and password='%s'" % (name, password)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return True
        else:
            return False

    def query1(self,word):
        sql="select mean from wordss where word='%s'"%word
        self.cur.execute(sql)
        r=self.cur.fetchone()
        if r:
            return r[0]

    def insert_hist(self,name,word):
        sql="insert into hist (name,word) values(%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def hist(self,name):
        sql = "select name,word,time from hist where name='%s' \
              order by time desc limit 10"%name
        self.cur.execute(sql)
        many_row = self.cur.fetchall()
        return many_row

