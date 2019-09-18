import pymysql
#建立连接（鼠标选中函数名，按crtl+点击,查看函数参数）
#可以按顺序直接传参，也可以按关键字传参
# con = pymysql.connect('localhost', 'root', '123456','country', port=3306, charset='utf8')
con =pymysql.connect(host='localhost',port=3306,user='root',
                   password='123456',database='test',charset='utf8')

#获取游标
cur = con.cursor()
#插入数据
data_list = []
for x in range(2000000):
    name = 'xixi_%s'%(x)
    data_list.append(name)
    # 一条数据通信一次
    # cur.execute(ins)


ins = 'insert into students(name) values(%s)'
##数据达到某一个量的时候通信一次。直到全部传完，停止通信。
cur.executemany(ins, data_list)
con.commit()

#关闭
cur.close()
con.close()