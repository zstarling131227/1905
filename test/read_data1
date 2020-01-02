import pymysql
import os
import re
import chardet

db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='123456', database="mobile", charset='utf8')

def get_filename(path):
    for info in os.listdir(r'%s' % path):
        domain = os.path.abspath(r'%s' % path)
        info = os.path.join(domain, info)
        print(info)
        if "." not in str(info):
            get_filename(info)
        else:
            read_data(info)

def get_encoding(file):
    with open(file,"rb") as f:
        print(chardet.detect(f.read())["encoding"])
        return chardet.detect(f.read())["encoding"]

def read_data(file):
    # print(file)
    # for info in os.listdir('%s' % file):
    #     domain = os.path.abspath('%s' % file)
    #     info = os.path.join(domain, info)
    with open(file, encoding=get_encoding(file)) as f:
        for line in f:
            if len(line) > 10:
                # print(line)
                phonenumber = re.findall(r"^[1][34578][0-9]{9}", line)
                # print(phonenumber)
                if phonenumber:
                    phonenumber = phonenumber[0]
                else:
                    continue
                cur = db.cursor()
                sql = 'insert into phone values("%s");' % phonenumber
                cur.execute(sql)
            else:
                continue
    db.commit()
    print("%s完成" % file)
    cur.close()


re = get_filename("H:\\muqia_data\\链接\\渠道反馈数据\\test")
db.close()
print(re)
