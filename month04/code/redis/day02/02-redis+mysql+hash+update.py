import redis
import pymysql


class Update(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='123456', database='userdb', charset='utf8')
        self.cursor = self.db.cursor()
        self.r = redis.Redis('localhost', 6379, 1)

    def update_mysql(self, new_score, username):
        sel = 'update user set score= %s where name=%s'
        try:
            self.cursor.execute(sel, [new_score, username])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print('Failed', e)

    def update_redis(self, new_score, username):
        result = self.r.hgetall(username)
        print(result)
        if result:
            self.r.hset(username, 'score', new_score)
        else:
            self.select_mysql(username)

    def select_mysql(self, username):
        sel = 'select age,gender,score from user where name=%s'
        self.cursor.execute(sel, [username])
        userinfo = self.cursor.fetchall()  # #返回值为元组
        if not userinfo:
            print('用户不存在')
        else:
            print('mysql', userinfo)
        user_dict = {
            'age': userinfo[0][0],
            'gender': userinfo[0][1],
            'score': userinfo[0][2],
        }
        self.r.hmset(username, user_dict)
        self.r.expire(username, 120)

    def main(self):
        username = input('请输入用户名：')
        new_score = input("请输入成绩：")
        if self.update_mysql(new_score, username):
            self.update_redis(new_score, username)
        else:
            print('更新失败')


if __name__ == '__main__':
    sp = Update()
    sp.main()
