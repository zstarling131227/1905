import pymysql
db=pymysql.connect(
    'localhost','root','123456','maoyandb',charset='utf8'
)
cursor=db.cursor()
ins='insert into filmset values(%s,%s,%s)'
data_list=[
    ['西游记','张惠妹','1997'],
    ['公主小妹','张韶涵','1998']
]
cursor.executemany(ins,data_list)
db.commit()
cursor.close()
db.close()