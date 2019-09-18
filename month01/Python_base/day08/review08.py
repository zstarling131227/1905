############练习1
"""
    练习1:定义计算四位整数，每位相加和的函数.
    测试："1234"   "5428"
"""
# def each_unit_sum(interger):
#     """
#
#     :param interger: 四位数
#     :return: 相加值结果
#     """
#     result = interger % 10
#     result += (interger % 100) // 10
#     result += (interger % 1000) // 100
#     result += interger // 1000
#     # gewei = interger % 10
#     # shiwei=(interger%100)//10
#     # baiwei=(interger%1000)//100
#     # qianwei=interger//1000
#     # result=gewei+shiwei+baiwei+qianwei
#     return result
#
# interger = int(input("请输入一个四位数整数："))
# a = each_unit_sum(interger)
# print("各位数相加的和是：", a)

###########练习2
"""
练习2:定义根据两,计算几斤零几两的函数
weight_liang = int(input("请输入两："))
jin = weight_liang // 16
liang = weight_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")
"""
# def calculate_jin_liang(data):
#     """
#     根据两，计算几斤几两
#     :param data: 需要计算的两
#     :return: 元组（斤，两）
#     """
#     jin=data//16
#     liang=data%16
#     return (jin,liang)#####返回的也可以是列表，或字典等任何容器。\
#     # 若返回的直接是jin,liang ,不加括号表示的是元组。
# data=int(input("请输入一个数:"))
# re=calculate_jin_liang(data)
# print(re[0],"斤",re[1],"两")

############练习3
"""
练习:定义 根据成绩计算等级 的函数
score = int(input("请输入成绩："))
if score > 100 or score < 0:
    print("输入有误")
elif 90 <= score:
    print("优秀")
elif 80 <= score:
    print("良好")
elif 60 <= score:
    print("及格")
else:
    print("不及格")
"""
# def get_grade_rank(grade):
#     """
#     对学生分数标记等级
#     :param grade: 学生分数
#     :return: 学生等级
#     """
#     # if 0>grade or grade>100:
#     #     return ("输入有误")
#     # elif 90<=grade:
#     #     return ("优秀")
#     # elif 80<=grade:
#     #     return ("良好")
#     # elif 60<=grade:
#     #     return "及格"####加不加括号都可以
#     # else:
#     #     return ("不及格")
#     if 0>grade or grade>100:
#         return ("输入有误")########return 已经具有退出函数的作用，所以无需再判断是否存在互斥性
#     if 90<=grade:
#         return ("优秀")
#     if 80<=grade:
#         return ("良好")
#     if 60<=grade:
#         return "及格"
#     return "不及格"
# data=int(input("请输入一个数:"))
# re=get_grade_rank(data)
# print(re)
############练习4
"""
练习:定义　判断列表中是否存在相同元素的　函数
list01 = [3, 81, 3, 5, 81, 5]
result = False
for r in range(0, len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] == list01[c]:
            print("具有相同项")
            result = True
            break  # 退出循环
    if result:
        break
if result == False:
    print("没有相同项")
"""
######自己写的代码定义
# def if_same_num(list_target):
#     for i in range(len(list_target)):
#         for j in range(len(list_target)):
#             if list_target[i] == list_target[j] and i!=j:
#                 return (list_target[i])
########老师写的代码定义
# def if_same_num(list_target):
#     for r in range(0, len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] == list_target[c]:
#                 return True#######("具有相同项")
#     return False#####ｆａｌｓｅ也可以写成"没有相同项"，但是只有两种结果时，建议使用ｔｒｕｅ和ｆａｌｓｅ或者０和１
# list_target = [3, 80, 45, 5, 80, 1]
# list01=if_same_num(list_target)
# print(list01)

############练习5
"""
定义函数,根据年月，计算有多少天。考虑闰年29天，平年28天（仔细看老师练习笔记，不建议的写法）
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误")
elif month == 2:
    print("２８天")
elif month in (4,6,9,11):
    print("３０天")
else:
    print("３１天")
"""

# ######下述为复杂写法：
# def caculate_days(year,month):
#     if month < 1 or month > 12:
#         return -1
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         else:
#             return 28
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     return 31
# ######下述为简单写法：
# def is_leap_year(year):
#     # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     #     return 29
#     # else:
#     #     return 28
#     #####上述为复杂写法
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# def caculate_days(year,month):
#     """
#
#     :param month: 月份
#     :param year: 年
#     :return: 该月天数####(return返回的结果一般为同类型，即同数值型或字符型或ｂｏｏｌ型等)
#     """
#     if month < 1 or month > 12:
#         return -1
#     if month == 2:
#         # if is_leap_year():
#         #     return 29
#         # else:
#         #     return 28
#         ######上述为复杂写法
#         return 29 if is_leap_year() else 28
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     return 31

############最终定义版本
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# def caculate_days(year,month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         return 29 if is_leap_year() else 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31
# days=caculate_days(2019,5)
# print(days)

###########老师讲
# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         return 29 if is_leap_year(year) else 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31
#
# print(get_day_by_month(2019,5))
############练习6
"""
定义列表升序排列的函数
list01= [43,4,5,6,7]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
"""

"""
    满足以下两个条件，就无需通过返回值传递结果。
    1.传入的是可变对象
    2.函数体修改的是传入的对象
"""
# ###########升序
# def decease_sort(list_target):
#     for i in range(len(list_target)-1):
#         for j in range(i+1, len(list_target)):
#                if list_target[i] > list_target[j]:
#                 list_target[i], list_target[j] = list_target[j], list_target[i]
#     # return list_target####无需ｒｅｔｕｒｎ
#
# list_target = [3, 80, 45, 5, 7, 1]
# decease_sort(list_target)
# print(list_target)

############练习7
"""
练习：定义方阵转置函数
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for c in range(1, len(list01)):  # 1 2 3
    for r in range(c, len(list01)):
        list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]
print(list01)
"""
# def transpose_square_matrix(squre_matrix):
#     """
#     方阵转置
#     :param squre_matrix:方阵
#     :return: 转置结果
#     """
#     for c in range(1, len(squre_matrix)):
#         for r in range(c, len(squre_matrix)):
#             squre_matrix[r][c - 1], squre_matrix[c - 1][r] = squre_matrix[c - 1][r], squre_matrix[r][c - 1]
# list_target = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
# transpose_square_matrix(list_target)
# print(list_target)
# transpose_square_matrix(list_target)
# print(list_target)
############练习8
"""
练习:记录一个函数fun01的执行次数.
     画出内存图
"""
# i = 0
# def fun01():
#     a = 100
#     global i
#     i += 1
# fun01()
# fun01()
# fun01()
# fun01()
# fun01()
# fun01()
# fun01()
# print("调用了%d次函数" % i)
############练习9
"""
练习:定义函数，根据小时，分钟，秒，计算总秒数.
要求：可以只计算小时-->秒
　　　可以只计算分钟-->秒
　　　可以只计算小时＋分钟-->秒
　　　可以只计算小时＋秒-->秒
"""
# ####def sum_second(hour,minute,second):########表示调用函数时必须填入３个实际参数
# def sum_second(hour=0,minute=0,second=0):#####随意填入参数
#     return hour*60**2+minute*60+second
# hour=int(input("请输入小时："))
# minute=int(input("请输入分钟："))
# second=int(input("请输入秒："))
# sum_second=sum_second(hour,minute,second)
# print("总秒数为:%d"%sum_second)

# #时＋分钟＋秒
# print(sum_second(4,56,7))
# #小时＋分钟
# print(sum_second(2,3))
# #分钟＋秒
# print(sum_second(minute=2,second=5))
# #分钟
# print(sum_second(minute=2))
# #小时
# print(sum_second(2))

############练习10
"""
练习:定义函数，数值相加的函数.
"""
# def add(*args):####参数无限个
#     # return sum(args)
#     result=0
#     for i in args:#####args是元组
#         result+=i
#     return result
#
# print(add(12,32,421,4))

