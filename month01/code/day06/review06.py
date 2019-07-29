#############练习1
"""
# 练习:使用range生成1--10之间的数字,将数字的平方存入list01中
# 将list01中所有奇数存入list02
# 将list01中所有偶数存入list03
# 将list01中所有偶数大于5的数字增加1后存入list04
"""
# list01=[]
# for i in range(1,11):
#     list01.append(i**2)
# list01=[i**2 for i in range(1,11)]
# print(list01)
# list02=[]
# for i in list01:
#     if i/2!=0:
#         list02.append(i)
# print(list02)
# list02=[i for i in list01 if i%2!=0]
# print(list02)
# list03=[i for i in list01 if i%2==0]
# print(list03)
# list04=[]
# for i in list01:
#     if i%2==0 and i>5:
#         list04.append(i+1)
# print(list04)
# list04=[i+1 for i in list01 if i%2==0 and i>5]
# print(list04)
#############练习2
"""
   练习:借助元组完成下列功能.
"""
# month = input("月份：")
# if month<"1" or month>"12":##############此处表示的是字符串的大小比较， 而不是数值大小的比较，故结果出错。修改方式为将month定义为整形，去掉双引号。
#     print("输入有误")
# elif month=="2":
#     print("28天")
# elif month=="4" or month=="6" or month=="9" or month=="11":
#     print("30天")
# else:
#     print("31天")
# #####方法1
# month =int(input("月份："))
# if month<1 or month>12:
#     print("输入有误")
# elif month=="2":
#     print("28天")
# elif month in (4,6,9,11):
#     print("30天")
# else:
#     print("31天")
# #######方法2
# month = int(input("月份："))
# if month<1 or month>12:
#     print("输入有误")
# else:
#     day_of_month=(31,28,31,30,31,30,31,31,30,31,30,31)
#     print(day_of_month[month-1])

#############练习3
"""
    练习:在控制台中录入日期(月日)，计算这是这一年的第几天.
    例如：３月５日
         1月天数 + 2月天数 + 5

         5月8日
         1月天数 + 2月天数 +3月天数 + 4月天数+ 8


    14:10
"""
###############自己做
# month=int(input("请输入月份:"))
# day=int(input("请输入天数:"))
# tuple01 = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# date = print("输入日期：%d月%d日" % (month, day))
# tuple02 = 0
# for i in range(month-1):
#     tuple02+=tuple01[i]
# print("这是这一年的第%d天"%(tuple02+day))
##########老师讲（切片法）
# print(sum(tuple01[:(month-1)])+day)

#############练习4
"""
    练习1:在控制台中循环录入商品信息(名称,单价).
    　　　如果名称输入空字符,则停止录入.
         将所有信息逐行打印出来.
    15:42
"""
# dict01={}
# while True:
#     name=input("请输入名称:")
#     # price=input("请输入单价:")
#     # if name=="":
#     #     break
#     ############if 如果在price的下一句，则在退出循环之前还会执行一次price语句，才能退出循坏。
#     if name=="":
#          break
#     price = int(input("请输入单价:"))
#     dict01["%s"%name]=price
#     # print(dict01)
# for k,v in dict01.items():
#     # print(k)##键#
#     # print(v)##值#
#     print("%s的单价是%d"%(k,v))

############练习5
"""
# 练习2: 在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
# 　　　如果名称输入空字符, 则停止录入.
# 将所有信息逐行打印出来.
"""

"""16:08
# 字典内嵌列表:
{
    "张无忌":[28,100,"男"],
}

"""
# dict01 = {}
# while True:
#     name = input("请输入名称:")
#     if name == "":
#         break
#     age = int(input("请输入年龄:"))
#     score = int(input("请输入分数:"))
#     sex = input("请输入性别:")
#     dict01[name] = [age, score, sex]
#     # print(dict01)

# ####取数据
# for name, list_info in dict01.items():#####此处的name和list_info是变量名，可以随便改
#     print("%s的年龄是%d,成绩是%d,性别是%s" % (name, list_info[0], list_info[1], list_info[2]))

# #############练习6
"""
# 字典内嵌字典:
{
    "张无忌":{"age":28,"score":100,"sex":"男"},
}
"""
# dit01_student_info = {}
# while True:
#     name = input("请输入名称:")
#     if name == "":
#         break
#     age = int(input("请输入年龄:"))
#     score = int(input("请输入分数:"))
#     sex = input("请输入性别:")
#     dict01_student_info[name] ##键= {"age": age, "score": score, "sex": sex}###值  ####给字典添加元素
#     # print(dict01)
# ####字典取数据
# for name, list_info in dict01_student_info.items():
#     print("%s的年龄是%d,成绩是%d,性别是%s" % (name, list_info["age"], list_info["score"], list_info["sex"]))

#############练习7
"""  
# 列表内嵌字典:
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"},
]
5:05 上课
"""
# list_student_info = []
# while True:
#     name = input("请输入名称:")
#     if name == "":
#         break
#     age = int(input("请输入年龄:"))
#     score = int(input("请输入分数:"))
#     sex = input("请输入性别:")
#     dict_info = {"name":name, "age": age, "score": score, "sex": sex}
#     list_student_info.append(dict_info)###列表添加元素
#     # print(list_student_info)
# ####列表取数据
# for dict_info in list_student_info:####与143行的变量名dict_info无关
#     print("%s的年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
# #######列表获取第一个学生信息
# dict_info###仅仅是定义一个变量名=list_student_info[0]
#############练习8（有问题）
"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.
"""
####字典套字典
# dit01_student_info = {}
# while True:
#     name = input("请输入名称:")
#     if name == "":
#         break
#     dit01_student_info[name]={}
#     i=1
#     while True:
#         hobby = input("请输第%d喜好:"%i)
#         sort="请输第%d个喜好:"%i
#         if hobby == "":
#             break
#         i+=1
#         dit01_student_info[name][sort] =hobby
    # print(dit01_student_info)
"""
输出结果为：
gdgd的喜好是
请输第1个喜好: gdgd
请输第2个喜好: gd
"""
# for name,value in dit01_student_info.items():
#     print("%s的喜好是"%name)
#     for key,hobby in value.items():
#         print("%s %s"%(key,hobby))
"""
输出结果为：
f的喜好是{'请输第1个喜好:': 'fs', '请输第2个喜好:': 'ds'}
"""
# for name,value in dit01_student_info.items():
#     print("%s的喜好是%s"%(name,value))

#########3列表内嵌字典
# list_person_bobby = []
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     dict_person = {name:[]}
#     list_person_bobby.append(dict_person)
#     while True:
#         bobby = input("请输入喜好：")
#         if bobby == "":
#             break
#         dict_person[name].append(bobby)
# print(list_person_bobby)
#
# for dict_info in list_person_bobby:
#     for key,value in dict_info.items():
#         print("%s的喜好是%s"%(key,value))

###########列表内嵌字典(喜好前有数字的类型)
list_student_info = []
while True:
    name = input("请输入名称:")
    if name == "":
        break
    list01=[]
    dict_person={name:[]}
    list_student_info.append(dict_person)
    i = 0
    while True:
        hobby = input("请输第%d个喜好:"%(i+1))
        if hobby == "":
            break
        i+=1
        dict_person[name].append("第%d个喜好是%s"%(i,hobby))

for dict_info in list_student_info:
    for key,value in dict_info.items():
        print("%s:%s"%(key,value))

for dict_info in list_student_info:
    for key,value in dict_info.items():
        print("%s:"%key)
        for i in value:
            print(i)

########字典套列表
dict_student_info = {}
while True:
    name = input("请输入名称:")
    if name == "":
        break
    dict_student_info[name]=[]   ##############指给字典dict_student_info的键赋值，而值为一个列表
    while True:
        hobby = input("请输喜好:")
        if hobby == "":
            break
        dict_student_info[name].append(hobby)   ##########此时的dict_student_info[name]指的是列表
print(dict_student_info)
for key,dict_info in dict_student_info.items():
    print("%s的喜好是%s"%(key,dict_info))
    # for i in dict_info:
    #     print(i)

###字典套列表(喜好前有数字的类型)
dict_student_info = {}
while True:
    name = input("请输入名称:")
    if name == "":
        break
    dict_student_info[name]=[]
    i=0
    while True:
        hobby = input("请输第%d个喜好:"%(i+1))
        if hobby == "":
            break
        i+=1
        dict_student_info[name].append("第%d个喜好是%s"%(i,hobby))
        #print(dict_student_info[name])
print(dict_student_info)
for key,dict_info in dict_student_info.items():
    # print("%s的喜好是%s"%(key,dict_info))
    print("%s的喜好是"%key)
    for i in dict_info:
        print(i)

