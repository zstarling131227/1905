####练习１
"""
# 练习：创建Enemy类对象，将对象打印在控制台中(格式自定义)
#      克隆Enemy类对象，体会克隆对象变量的改变不影响原对象。

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""
class Enemy:
    def __init__(self,name,hp,atk,defense):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.defense=defense
# """
# s01 = Enemy("王八蛋", 657, 56, 7575)
# print(s01)
# 输出结果为：<__main__.Enemy object at 0x7fa473a6aa58>
# """
    def __str__(self):
        return"他叫%s,编号是%d,年龄是%d,成绩是:%d"%(self.name,self.hp,self.atk,self.defense)
    def __repr__(self):
        return"Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)
# s01=Enemy("王八蛋",657,56,7575)
# print(s01)
# str02=repr(s01)
# print(str02)
# s02=eval(repr(s01))###克隆
# s02.name="老王"
# print(s02.name)
# print(s02)

####练习2
class Vector1:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "王八蛋是"+str(self.x)
    def __sub__(self, other):
        return Vector1(self.x-other)
    def __mul__(self, other):
        return "王八蛋"+"霰雪鸟"
    def __rsub__(self, other):
        return "王八蛋"
    def __rmul__(self, other):
        return Vector1(self.x*other)
    def __add__(self, other):
        return Vector1(self.x + other)
    def __radd__(self, other):
        return (self.x+other,str("王八蛋" + "霰雪鸟"))
    def __iadd__(self, other):
        self.x+=other
        return self


# v01=Vector1(10)
# print(v01-2)
# print(v01+2)
# print(2-v01)
# print(2*v01)
# print(2+v01)
# print(id(v01))
# v01+=56
# print(v01,id(v01))
#####练习３

#封装:将每一种影响效果单独做成类
#多态：各种影响效果在重写SkillImpactEffect类中的impact
class SkillImpactEffect:#父（继承）
    def impact(self):
        raise NotImplementedError()
#开闭原则，单一原则
class DamageEffect(SkillImpactEffect):#子（继承）
    def __init__(self,value):
        self.value=value
    def impact(self):
        print("扣你%d血量"%self.value)

class LowerDeffenseEffect(SkillImpactEffect):#子（继承）
    def __init__(self, value,time):
        self.value = value
        self.time=time
    def impact(self):
        print("降低%d防御力，持续%d秒" % (self.value,self.time))

class DizzinessEffect(SkillImpactEffect):#子（继承）
    def __init__(self, time):
        self.time=time
    def impact(self):
        print("眩晕%d秒" % self.time)

class SkillDeployer:
    def __init__(self,name):
        self.name=name
        self.__dict_skill_config=self.__load_config_file()#组合复用原则
        self.__effect_objects=self.__creat_effect_objects()
    def __load_config_file(self):
        return {
            "降龙十八掌":["DamageEffect(200)","LowerDeffenseEffect(-10,5)","DizzinessEffect(2)"] ,
            "六面神剑":["DamageEffect(100)","LowerDeffenseEffect(-10,5)","DizzinessEffect(2)"]

        }
    def __creat_effect_objects(self):
        list_effect_name=self.__dict_skill_config[self.name]
        list_effect_object=[]
        for item in list_effect_name:
            list_effect_object.append(eval(item))###eval将字变成对象
        return list_effect_object
    def generate_skill(self):
        print(self.name,"技能释放了")
        for item in self.__effect_objects:
            item.impact()

# xlsbz=SkillDeployer("降龙十八掌")
# xlsbz.generate_skill()

#####练习４
"""
    将day11/day10_exercise/exercise01.py中的
    练习1：Vector2和DoubleListHelper定义到
          double_list_helper.py模块中.
"""
#day14中多出一个double_list_helper.py文件。
"""
    练习2:在exercise03.py模块中，实现
        (1)在二维列表中，获取13位置，向左，3个元素

        (2)在二维列表中，获取22位置，向上，2个元素

        (3)在二维列表中，获取03位置，向下，2个元素
    要求：使用三种导入方式
    体会：哪一种更合适。
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
"""

####在练习１的基础上，将ｄａｙ1４标记为根目录导入
# 导入方式1
import double_list_helper as d01

# 在二维列表中，获取13位置，向左，3个元素
re1 = d01.DoubleListHelper.get_elements(list01, d01.Vector2(1, 3), d01.Vector2.left(), 3)
for item in re1:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re2 = d01.DoubleListHelper.get_elements(list01, d01.Vector2(2, 2), d01.Vector2.up(), 2)
for item in re2:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re3 = d01.DoubleListHelper.get_elements(list01, d01.Vector2(0, 3), d01.Vector2.down(), 2)
for item in re3:
    print(item)
    
    
# 导入方式2
from double_list_helper import DoubleListHelper as d02
from double_list_helper import Vector2 as d03

# 在二维列表中，获取13位置，向左，3个元素
re1 = d02.get_elements(list01, d03(1, 3), d03.left(), 3)
for item in re1:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re2 = d02.get_elements(list01, d03(2, 2), d03.up(), 2)
for item in re2:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re3 = d02.get_elements(list01, d03(0, 3), d03.down(), 2)
for item in re3:
    print(item)

from double_list_helper import DoubleListHelper
from double_list_helper import Vector2

# 在二维列表中，获取13位置，向左，3个元素
re1 = DoubleListHelper.get_elements(list01,Vector2(1, 3),Vector2.left(), 3)
for item in re1:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re2 = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
for item in re2:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re3 = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
for item in re3:
    print(item)
    
    
# 导入方式3
from double_list_helper import *

# 在二维列表中，获取13位置，向左，3个元素
re1 = DoubleListHelper.get_elements(list01,Vector2(1, 3),Vector2.left(), 3)
for item in re1:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re2 = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
for item in re2:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re3 = DoubleListHelper.get_elements(list01, Vector2(0, 3),Vector2.down(), 2)
for item in re3:
    print(item)
"""

"""
# 导入方式1
# 本质：使用变量名module01关联模块地址
####将ｄａｙ10中的ｅｘｅｒｃｉｓｅ１０标记为根目录导入
# as 为导入的成员其另外一个名称
import exercise10 as m01
# 在二维列表中，获取13位置，向左，3个元素
re = m01.DoubleListHelper.get_elements(list01, m01.Vector2(1, 3), m01.Vector2.left(), 3)
for item in re:
    print(item)
# 导入方式2
# 本质：将指定的成员导入到当前模块作用域中
# 小心：导入进来的成员不要和当前模块成员名称相同
from exercise10 import DoubleListHelper as m02
from exercise10 import Vector2
for item in re:
    print(item)
# 在二维列表中，获取13位置，向左，3个元素
re = m02.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)

# 导入方式3
# 本质：将指定模块的所有成员导入到当前模块作用域中
# 小心：导入进来的成员和其他模块成员冲突
from exercise10 import *
# 在二维列表中，获取13位置，向左，3个元素
re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
for item in re:
    print(item)
"""

