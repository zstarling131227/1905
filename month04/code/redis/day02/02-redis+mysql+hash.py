import redis
import pymysql

r = redis.Redis('localhost', 6379, 1)
db = pymysql.connect(host='localhost', user='root', password='123456', database='userdb', charset='utf8')
cursor = db.cursor()
username = input('请输入用户名：')
result = r.hgetall(username)
if result:
    print('redis:', result)
else:
    sel = 'select * from user where name=%s'
    cursor.execute(sel, [username])
    userinfo = cursor.fetchall()  # #返回值为元组
    if not userinfo:
        print('用户不存在')
    else:
        print('mysql', userinfo)
        user_dict = {
            'name': userinfo[0][1],
            'age': userinfo[0][2],
            'gender': userinfo[0][3],
        }
        r.hmset('user', user_dict)
        r.expire('user', 30)
