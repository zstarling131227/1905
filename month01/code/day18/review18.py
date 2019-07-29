class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list_target = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]
'''
################## 练习１：
"""
    在list_helper.py中增加通用的求和方法.
    案例1:计算敌人列表中所有敌人的总血量.
    案例2:计算敌人列表中所有敌人的总攻击力.
    案例3:计算敌人列表中所有敌人的总防御力.
    步骤：
    实现具体功能/提取变化/提取不变/组合
"""

#实现具体功能
# def sum_enemy1():
#     sum_value = 0
#     for i in list01:
#         sum_value += i.hp
#     return sum_value
#
#
# def sum_enemy2():
#     sum_value = 0
#     for i in list01:
#         sum_value += i.defense
#     return sum_value
#
#
# def sum_enemy3():
#     sum_value = 0
#     for i in list01:
#         sum_value += i.atk
#     return sum_value
#
# #/提取变化/
# def handle1(item):
#     return item.hp
#
#
# def handle2(item):
#     return item.atk
#
#
# def handle3(item):
#     return item.defense
#
# #提取不变/组合
# def sum_enemy(list_target, handle):
#     sum_value = 0
#     for item in list_target:
#         # sum_value+=i.atk
#         sum_value += handle(item)
#     return sum_value

# from common.list_helper import *
# print("-----------------------")
# g01 = ListHelper.sum_enemy(list01,handle2)
# print(g01)
#
# g06 = ListHelper.sum_enemy(list01,lambda item:item.atk)
# print(g06)
# print("-----------------------")
# g05 = ListHelper.sum_enemy(list01,handle1)
# print(g05)
#
# g04 = ListHelper.sum_enemy(list01,lambda item:item.hp)
# print(g04)
# print("-----------------------")
# g03 = ListHelper.sum_enemy(list01,handle3)
# print(g03)
#
# g02 = ListHelper.sum_enemy(list01,lambda item:item.defense)
# print(g02)
'''

'''
##############练习２
"""
    练习2:
    在list_helper.py中增加通用的筛选方法.
    案例1:获取敌人列表中所有敌人的名称.
    案例2:计算敌人列表中所有敌人的攻击力.
    案例3:计算敌人列表中所有敌人的名称和血量.
"""
# def cancle():
#     list_result=[]
#     for item in list01:
#         list_result.append(item.name)
#     return list_result
# print(cancle())

# def con1(item):
#     return item.name
# def con2(item):
#     return item.atk
# def con3(item):
#     return item.name,item.defense

# def cancle(list_target, con):
#     list_result = []
#     for item in list_target:
#         list_result.append(con(item))
#     return list_result

# def cancle1(list_target, con):
#     for item in list_target:
#         yield con(item)

#
# from common.list_helper import *

# print("-----------------------")
# g05 = ListHelper.cancle(list01,con1)
# print(g05)
# g01 = ListHelper.cancle(list01,con2)
# print(g01)
# g03 = ListHelper.cancle(list01,con3)
# print(g03)
#
# print("-----------------------")
# g06 = ListHelper.cancle(list01,lambda item:item.name)
# print(g06)
#
# g04 = ListHelper.cancle(list01,lambda item:item.atk)
# print(g04)
#
# g02 = ListHelper.cancle(list01,lambda item:(item.name,item.defense))
# print(g02)
#
# print("-----------------------")
# g07 = ListHelper.cancle1(list01,lambda item:item.name)
# for i in g07:
#     print(i)
#
# g08 = ListHelper.cancle(list01,lambda item:item.atk)
# for i in g08:
#     print(i)
#
# g09 = ListHelper.cancle(list01,lambda item:(item.name,item.defense))
# for i in g09:
#     print(i)
'''

'''
######练习３
"""
    练习3:
    在list_helper.py中增加通用的获取最大值方法.
    案例1:获取敌人列表中攻击力最大的敌人.
    案例2:获取敌人列表中防御力最大的敌人.
    案例3:获取敌人列表中血量最高的敌人.
"""
######输出结果为最大值的数据（为一个数）
# def max_enemy():
#     max_value = list_target[0].atk
#     for item in range(len(list_target)):
#         if max_value<list_target[item].atk:
#             max_value=list_target[item].atk
#     return max_value
# print(max_enemy())
#
# def max_enemy(list_target, con):
#     max_value = con(list_target[0])
#     for item in range(len(list_target)):
#         if max_value<con(list_target[item]):
#             max_value=con(list_target[item])
#     return max_value
#
# print("-----------------------")
# g10 = max_enemy(list_target, lambda item:item.defense)
# print(g10)
#
# g11 = max_enemy(list_target, lambda item:item.atk)
# print(g11)
#
# g12 = max_enemy(list_target, lambda item:item.hp)
# print(g12)
#
#
# from common.list_helper import *
# print("-----------------------")
# g10 = ListHelper.max_enemy(list_target, lambda item:item.defense)
# print(g10)

# g11 = ListHelper.max_enemy(list_target, lambda item:item.atk)
# print(g11)
#
# g12 = ListHelper.max_enemy(list_target, lambda item:item.hp)
# print(g12)

######输出结果为最大值的一个技能（为技能的所有值）
# def max_enemy1():
#     max_value= list_target[0]
#     for item in range(1,len(list_target)):
#         if max_value.atk < list_target[item].atk:
#             max_value = list_target[item]
#     return max_value
# print(max_enemy1())

#####此时的item指的是列表中的每一项技能
# def con1(item):
#     return item.atk
#
# def con2(item):
#     return item.hp
#
# def con3(item):
#     return item.defense
#
# def max_enemy1(list_target, con):
#     max_value = list_target[0]
#     for item in range(len(list_target)):
#         if con(max_value)<con(list_target[item]):
#             max_value=list_target[item]
#     return max_value
#

# from common.list_helper import *
# print("-----------------------")
# g10 = ListHelper.max_enemy1(list_target, lambda item:item.defense)
# print(g10)
#
# g11 = ListHelper.max_enemy1(list_target, lambda item:item.atk)
# print(g11)
#
# g12 = ListHelper.max_enemy1(list_target, lambda item:item.hp)
# print(g12)
'''

''''''
#######练习４
"""
    练习4:
    在list_helper.py中增加通用的升序排列方法.
    案例1:将敌人列表按照攻击力进行升序排列.
    案例2:将敌人列表按照防御力进行升序排列.
    案例3:将敌人列表按照血量进行升序排列.
"""
# def sort_enemy():
#     for i in range(len(list01)):
#         for j in range(i, len(list01)):
#             if list01[i].atk < list01[j].atk:
#                 list01[j],list01[i] = list01[i],list01[j]
#     return list01
# e01=sort_enemy()
# for i in e01:
#     print(i)

# def sort_enemy():
#     for i in range(len(list01)):
#         for j in range(i, len(list01)):
#             if list01[i].atk < list01[j].atk:
#                 list01[j],list01[i] = list01[i],list01[j]
    # return list01

# def con1(item):
#     return item.hp
# def con2(item):
#     return item.defense
# def con3(item):
#     return item.atk

# def sort_enemy(list_target,con):
#     for i in range(len(list_target)):
#         for j in range(i,len(list_target)):
#             if con(list_target[i]) < con(list_target[j]):
#                 list_target[j],list_target[i] = list_target[i],list_target[j]
#     return list_target

######下述方法不需要return
# e01=sort_enemy(list01,con1)
# for item in list01:
#     print(item)
# print("--------------------------")
# e05=sort_enemy(list01,lambda item:item.atk)
# for i in e05:
#     print(i)
# e02=sort_enemy(list01,lambda item:item.atk)
# for i in e02:
#     print(i)


#####导入模块版
# print("--------------------------")
# from common.list_helper import *

# e02=ListHelper.sort_enemy(list01,lambda item:item.atk)
# for i in e02:
#     print(i)
#
# print("--------------------------")
# e03=ListHelper.sort_enemy(list01,lambda item:item.hp)
# for i in e03:
#     print(i)

from common.list_helper import *

print("--------------------------")
e04=ListHelper.sort_enemy1(list01,lambda item:item.defense)
for i in e04:
    print(i)

######下述方法不需要return
print("--------------------------")
ListHelper.sort_enemy(list01, lambda item: item.hp)
for item in list01:
    print(item)
'''
#######练习5
"""
    内置高阶函数
    练习:
    1. ([1,1,1],[2,2],[3,3,3,3])
       获取元组中，长度最大的列表.
    2. 根据敌人列表，获取所有敌人的姓名与血量与攻击力.
    3.　在敌人列表中，获取攻击力大于100的所有活人.
    4. 根据防御力对敌人列表进行降序排列.
"""
##########    获取元组中，长度最大的列表.
# tuple01=([1,1,1,1],[2,2,2],[3,3,3,3,3])
# print(max(tuple01,key=lambda item:len(item)))

##########    2. 根据敌人列表，获取所有敌人的姓名与血量与攻击力.
# from common.list_helper import *
# print("-------------")
# e3=ListHelper.cancle(list_target,lambda item:(item.name,item.hp,item.atk))
# for i in e3:
#     print(i)

# print("_____________")
# e03=map(lambda item:(item.name,item.hp,item.atk),list_target)
# for i in e03:
#     print(i)

#################  3.　在敌人列表中，获取攻击力大于100的所有活人.
# print("-------------")
# e2=ListHelper.find_all(list_target,lambda item:item.hp>0 and item.atk>100)
# for i in e2:
#     print(i)
# print("_____________")
# e02=filter(lambda item:item.atk>100 and item.hp>0,list_target)
# for i in e02:
#     print(i)

###########    4. 根据防御力对敌人列表进行降序排列.
# print("-------------")
# e01=sorted(list_target,key=lambda item:item.defense,reverse=True)
# for i in e01:
#     print(i)
'''








