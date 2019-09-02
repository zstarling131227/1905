class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]
"""
作业
1.三合一（闭包）
2.当天练习独立完成(list_helper.py)
3.在list_helper.py中新增以下功能：
    (1)获取最小值
    (2)降序排列
    (3)根据指定条件删除元素
       案例:在敌人列表中，删除所有死人.
       案例:在敌人列表中，攻击力小于50的所有敌人.
       案例:在敌人列表中，防御力大于100的所有敌人.
4. 阅读"面向对象答辩优胜者"文档.
   总结出属于自己的话术，以便就业准备简历时使用(介绍项目).
"""
from common.list_helper import *

'''
#####最小值
print("-----------------------")
g10 = ListHelper.min_enemy1(list01, lambda item:item.defense)
print(g10)

g11 = ListHelper.min_enemy1(list01, lambda item:item.atk)
print(g11)

g12 = ListHelper.min_enemy1(list01, lambda item:item.hp)
print(g12)

print("-----------------------")
g10 = ListHelper.min_enemy(list01, lambda item:item.defense)
print(g10)

g11 = ListHelper.min_enemy(list01, lambda item:item.atk)
print(g11)

g12 = ListHelper.min_enemy(list01, lambda item:item.hp)
print(g12)

######升序
from common.list_helper import *

print("--------------------------")
e02=ListHelper.sort_enemy(list01,lambda item:item.atk)
for i in e02:
    print(i)

print("--------------------------")
e03=ListHelper.sort_enemy(list01,lambda item:item.hp)
for i in e03:
    print(i)

print("--------------------------")
e04=ListHelper.sort_enemy(list01,lambda item:item.defense)
for i in e04:
    print(i)
'''
"""
(3)根据指定条件删除元素
       案例:在敌人列表中，删除所有死人.
       案例:在敌人列表中，攻击力小于50的所有敌人.
       案例:在敌人列表中，防御力大于100的所有敌人.
"""
print("--------------------------")
'''
#
# def del_enemy1():
#     for item in range(len(list01) - 1, -1, -1):
#         # print(item)
#         # print(list01[item].hp)
#         if list01[item].hp == 0:
#             list01.remove(list01[item])
#     return list01
#
# del_enemy1()


# def del_enemy2():
#     for item in range(len(list01) - 1, -1, -1):
#         # print(item)
#         print(list01[item].atk)
#         if list01[item].atk < 150:
#             list01.remove(list01[item])
#     return list01
#
# del_enemy2()

#
# def del_enemy3():
#     for item in range(len(list01) - 1, -1, -1):
#         # print(item)
#         print(list01[item].defense)
#         if list01[item].defense > 100:
#             list01.remove(list01[item])
#     return list01
#
# del_enemy3()

# def con1(item):
#     return item.hp==0
# def con2(item):
#     return item.defense>100
# def con3(item):
#     return item.atk<150
#
# def del_enemy(list_target,con):
#     for item in range(len(list_target) - 1, -1, -1):
#         if con(list_target[item]):
#             list_target.remove(list_target[item])
#     return list_target

# print("--------------")
# e01=del_enemy(list01,con1)
# for i in e01:
#     print(i)
#
# e02=del_enemy(list01,con2)
# for i in e02:
#     print(i)
#
# e03=del_enemy(list01,con3)
# for i in e03:
#     print(i)

# print("--------------")
# e04=del_enemy(list01,lambda item:item.hp==0)
# for i in e04:
#     print(i)
#
# e05=del_enemy(list01,lambda item:item.defense>100)
# for i in e05:
#     print(i)
#
# e06=del_enemy(list01,lambda item:item.atk<150)
# for i in e06:
#     print(i)

from common.list_helper import *

print("--------------")
e04=ListHelper.del_enemy(list01,lambda item:item.hp==0)
for i in e04:
    print(i)

print("--------------")
e05=ListHelper.del_enemy(list01,lambda item:item.defense>100)
for i in e05:
    print(i)

print("--------------")
e06=ListHelper.del_enemy(list01,lambda item:item.atk<150)
for i in e06:
    print(i)
'''

'''

#####没有return,且删除用的是del 语句，而不是ｒｅｍｏｖｅ.
# ListHelper.del_enemy1(list01,lambda item:item.hp==0)
# for item in list01:
#     print(item)

# print("--------------------------")
# ListHelper.del_enemy1(list01,lambda item:item.defense<100)
# for item in list01:
#     print(item)

# print("--------------------------")
# ListHelper.del_enemy1(list01,lambda item:item.atk>100)
# for item in list01:
#     print(item)

'''