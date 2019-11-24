import pymysql
import os
import re

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='123456', database="read_data", charset='utf8')


def get_filename(path):
    for info in os.listdir(r'%s' % path):
        domain = os.path.abspath(r'%s' % path)
        info = os.path.join(domain, info)
        print((type(info)))
        if os.path.isfile(info):
            read_data(info)
        else:
            get_filename(info)


def read_data(file):
    with open(file, encoding='utf-8') as f:
        for line in f:
            if len(line) > 10:
                # print(line)
                phonenumber = re.findall(r"^[1][34578][0-9]{9}", line)
                # print(phonenumber)
                phonenumber = phonenumber[0]
                cur = db.cursor()
                sql = 'insert into mobile values("%s");' % phonenumber
                cur.execute(sql)
            else:
                continue
    db.commit()
    print("%s完成" % file)
    # get_filename()
    cur.close()



re = get_filename("/home/tarena/中信还呗民生2019可再利用数据")
db.close()
print(re)
