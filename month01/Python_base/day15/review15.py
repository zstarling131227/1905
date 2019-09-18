####练习１
import time
def get_week(year,month,day):#面向对象的方法
    # print(time.strptime(str_time01, "%Y / %m / %d %H:%M:%S"))
    tuple_time01=time.strptime("%d / %d / %d"%(year,month,day), "%Y / %m / %d")
    # # print(tuple_time[1]) # 获取月
    # print(tuple_time01[6]) # 获取星期,其返回值为０，１，２，３，４，５，６
    """
     #错误代码。应该使用ｉｆ语句，然后逐步修改为字典。
      tuple_time02=time.localtime()
      for item in range(tuple_time01,tuple_time02):
         str_time02=time.strftime("星期%w", item)
         print(str_time02)
     """
    """
    ###低级写法
    if tuple_time01[6]==0:
        return "星期一"
    if tuple_time01[6]==1:
        return "星期二"
    if tuple_time01[6]==2:
        return "星期三"
    ……(中文符号下shift+F6打印省略号)
    """
    dict_weeks={
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",
        6:"星期七",
    }
    return dict_weeks[tuple_time01[6]]###根据字典的键获取值

# get_week(2019,6,20)###含有ｒｅｔｕｒｎ时，此种情形下输出结果为空。不含ｒｅｔｕｒｎ，有ｐｒｉｎｔ值时，输出结果为ｐｒｉｎｔ的结果。
# re=get_week(2019,6,15)
# print(re)###含有ｒｅｔｕｒｎ时，此种情形下输出结果为"星期ｘ"

####练习２
"""
# 练习2：根据生日(年月日)，计算活了多少天。
# 思路：
# 年月日 --> 出生时间
# 当前时间 --> 出生时间
# 计算天
"""
def get_birth(year,month,day):
    tuple_time01 = time.strptime("%d / %d / %d" % (year, month, day), "%Y / %m / %d")
    #####自己写的，计算的是总天数。
    print(tuple_time01)##目的：调试
    print(tuple_time01[7])
    tuple_time02=time.localtime()
    print(tuple_time02)
    print(tuple_time02[7])
    year_days=(tuple_time02[0]-tuple_time01[0])*365
    #　出现误差是因为有闰年[1996, 2000, 2004, 2008, 2012, 2016]，
    # 闰年一年有３６６天，平年一年有３６５天，而此处按统一３６５天计算。
    # 判断闰年的代码在ｄａｙ06下的exercise06中。
    print(year_days)
    day=year_days-tuple_time01[7]+tuple_time02[7]
    print(day)###输出结果为：8318

    # 老师讲
    # str02=time.time() ###获取当前时间戳(从1970年1月1日到现在经过的秒数)
    # return str02
    # str01=time.mktime(tuple_time01)######时间元组 --> 时间戳(计算从1970年1月1日到某一时间经过的秒数)
    # return str01
    # 从出生到当前日期的总秒数
    # life_second=time.time()-time.mktime(tuple_time01)
    # return life_second
    # 从出生到当前日期的总分钟
    # return life_second/60
    # 从出生到当前日期的总天数
    # return life_second/60/60//24###8324

# re=get_birth(1996,9,4)
# print(re)

def life_days(year, month, day):
    """
        根据生日计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 活的天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second = time.time() - time.mktime(tuple_time)
    return int(life_second / 60 / 60 // 24)

# print(life_days(1996,9,4))###8324

####练习３
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# print (time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
#
# print (time.strftime("%U %c %d %H:%M:%S %Y", time.localtime()))
#
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
#
# print (time.strftime("%A %B %d %I:%M:%S %Y", time.localtime()))
#
# print (time.strftime("%w %m %d %H:%M:%S %Y", time.localtime()))
#
# print (time.strftime("%W %m %j %H:%M:%S %y", time.localtime()))

# a = "Sat Mar 28 22:24:24 2016"
# print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# week_time=time.localtime()
# # 获取星期,其返回值为０，１，２，３，４，５，６
# #             星期一，二，三，四，五，六，日
# print(week_time[6])
# ## %w 星期（0-6），星期天为星期的开始
# # 获取星期,其返回值为０，１，２，３，４，５，６
# #             星期日，一，二，三，四，五，六
# print (time.strftime("%w ", week_time))

# import calendar
# print(calendar.month(1996,9))

####练习４
"""
    定义函数，在控制台中获取成绩的函数.
    要求：如果异常，继续获取成绩，直到得到正确的成绩为止.
         成绩还必须在0--100之间
    17:05
"""
def get_score():
    while 1:
        str_result=input("请输入成绩：")
        try:
            score = int(str_result)
            return score
        except:
            print("输入的不是整数")
            continue
        # if 0 < score < 100:
        #     return score
        # else:
        #     print("超出范围")
print(get_score())

####练习５
"""
    练习:敌人类(攻击力0--100)
        抛出异常的信息：消息/错误行/攻击力/错误编号
"""

class EnemyError(Exception):
    def __init__(self,asd,dasd,fdsf,fddsf):
        super().__init__("出错啦啦啦")
        self.asd=asd
        self.dasd=dasd
        self.fdsf=fdsf
        self.fddsf=fddsf

class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 21 <= value <= 31:
            self.__atk = value
        else:
            raise EnemyError("超过我想要的范围啦",value,26,1001)

try:
    w01 = Enemy(81)
except EnemyError as e:
    print("请重新输入")
    print(e.fddsf)
    print(e.asd)
    print(e.dasd)

















