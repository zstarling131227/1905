"""
作业:
1. 三合一
2. 当天练习独立完成
5. 阅读：
　　　HeadFirst设计模式
　　　重构　
6. 以班级为单位,评选最佳笔记,交给高娜老师.
   提醒项目经理老师，交面向对象答辩优胜作品.
"""
"""
3. 定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
（day 10）
"""
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "技能数据是:%s,%d,%d,%d" % (self.name, self.hp, self.atk, self.defense)

list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]


# from common.list_helper import *

# g01=ListHelper1.find_single(list01,lambda item:item.name=="灭霸")
# print(g01)
# print("--------------------------------")
#
# g02=ListHelper.find_all(list01,lambda item:item.atk>100)
# for i in g02:
#     print(i)
# print("--------------------------------")
#
# g03=ListHelper1.find_lambda(list01,lambda item:item.hp>0)
# print(g03)
# print("--------------------------------")

"""
4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
   案例1:判断敌人列表中是否存在"成昆"
   案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
    步骤:
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list_helper.py中
    体会：函数式编程的思想("封装，继承，多态")
"""
# def condition01(item):
#     return item.name=="成昆"

# def condition02(item):
#     return item.atk<5 or item.defense>10

# def find_emeny(list_target,fun_condition):
#     for item in list_target:
#         if fun_condition(item):
#             return True
# print(find_emeny(list01,condition01))
# print(find_emeny(list01,condition02))
# print("-----------------------")
from common.list_helper import *
g01=ListHelper1.find_emeny(list01,lambda item:item.name=="成昆")
print(g01)

print("-----------------------")
# print(ListHelper1.find_emeny(list01,condition02))
g01=ListHelper1.find_emeny(list01,lambda item:item.atk<5 or item.defense>10)
print(g01)
