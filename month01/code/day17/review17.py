#######练习１###解析enumerate过程
"""
    练习:定义生成器函数my_enumerate,实现下列现象.
         将元素与索引合成一个元组.
list01 = [3, 4, 55, 6, 7]
for item in enumerate(list01):
    # (索引,元素)
    print(item)

for index, element in enumerate(list01):
    print(index, element)
"""
# list01=[3,4,55,6,7]
# def my_enumerate(iterable_tarfet):
#     index=0
#     for i in iterable_tarfet:
#         yield index,i
#         index+=1
#     # for index in range(len(iterable_tarfet)):
#     #     yield [index,iterable_tarfet[index]]
# list02=my_enumerate(list01)
# print(list02)
# print(my_enumerate(list01))
"""
输出结果为：
<generator object my_enumerate at 0x7f00703f9d00>
"""
# for index,element in my_enumerate(list01):
#     print(index,element)
"""
输出结果为：
0 3
1 4
2 55
3 6
4 7
"""
#######练习２###解析ｚｉｐ过程
"""
# 练习: 定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02  = ["孙悟空","猪八戒","唐僧","沙僧"]
list03  = [101,102,103,104]
for item in zip(list02,list03):
    print(item)
"""
####下述是直接使用了zip 函数.
# list01=["孙悟空","猪八戒","唐僧","沙僧"]
# list02=[101,102,103,104]
# def my_zip(list01,list02):####参数的个数为两个，固定的
#     for item,value in zip(list01,list02):
#         yield item,value
# list03=my_zip(list01,list02)
# for item,value in list03:
#     print(item,value)
# for item,value in my_zip(list01,list02):
#     print(item,value)


###老师讲(解析zip 过程)
# list01=["孙悟空","猪八戒","唐僧","沙僧"]
# list02=[101,102,103,104]
# def my_zip(list01,list02):####参数的个数为两个，固定的
#     for i in range(len(list01)):
#         yield (list01[i],list02[i])
# for i in my_zip(list01,list02):
#     print(i)
"""
输出结果为：
('孙悟空', 101)
('猪八戒', 102)
('唐僧', 103)
('沙僧', 104)
"""
# list01=["孙悟空","猪八戒","唐僧","沙僧"]
# list02=[101,102,103,104]
# list03=["钥玥","王八蛋","嘻嘻","童话"]
# def my_zip(*args):####参数的个数为多个，不固定的（要求列表的长度相同）
#     for i in range(len(args[0])):
#         list_result=[]
#         for j in args:
#             list_result.append(j[i])
#         yield tuple(list_result)
# for i in my_zip(list01,list02,list03):
#     print(i)
"""
输出结果为：
('孙悟空', 101, '钥玥')
('猪八戒', 102, '王八蛋')
('唐僧', 103, '嘻嘻')
('沙僧', 104, '童话')
"""

# list01=["孙悟空","猪八戒","唐僧","沙僧"]
# list02=[101,102,103,104]
# list03=["钥玥","王八蛋","嘻嘻"]
# def my_zip(*args):####参数的个数为多个，不固定的（不要求列表的长度相同）
#     for item in args:
#         min_len=len(args[0])
#         if min_len>len(item):
#             min_len=len(item)
#     # print(min_len)
#     for i in range(min_len):
#         list_result=[]
#         for j in args:
#             list_result.append(j[i])
#         yield tuple(list_result)
# for i in my_zip(list01,list02,list03):
#     print(i)
"""
输出结果为：
('孙悟空', 101, '钥玥')
('猪八戒', 102, '王八蛋')
('唐僧', 103, '嘻嘻')
"""

#######练习３
"""
# 练习:获取列表中所有字符串
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.
"""
##生成器函数
# list01=[2,"ewqe",90,True,"xi","嘻嘻"]
# def find01(list_target):
#     for i in list_target:
#         if type(i)==str:
#             yield i
# re=find01(list01)
# for item in re:
#     print(item)

##生成器表达式
# list01=[2,"ewqe",90,True,"xi","嘻嘻",0.9,11.0,9.9]
# re=(i for i in list01 if type(i)==str)
# for item in re:
#     print(item)

##列表推导式
# re=[i for i in list01 if type(i)==str]
# for item in re:
#     print(item)


#######练习４
"""
# 练习： 获取列表中所有小数
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.
"""
##生成器函数
# list01=[2,"ewqe",90,True,"xi","嘻嘻",0.9,11.0,9.9]
# def find01(list_target):
#     for i in list_target:
#         if type(i)==float:
#             yield i
# re=find01(list01)
# for item in re:
#     print(item)

# 生成器表达式
# list01=[2,"ewqe",90,True,"xi","嘻嘻",0.9,11.0,9.9]
# re=(i for i in list01 if type(i)==float)
# for item in re:
#     print(item)
####上述简化版
# for item in (i for i in list01 if type(i)==float):
#     print(item)
####上述简化版改进
# for item in (i for i in list01 if type(i)==float):
#     print(item,end=" ")
####上述简化版改进(打出为列表形式)
# list02=[]
# for item in (i for i in list01 if type(i)==float):
#     list02.append(item)
# print(list02)

# 列表推导式
# re=[i for i in list01 if type(i)==float]
# for item in re:
#     print(item)

#######练习５
"""
    参照day10/exercise02.py
    完成下列练习
class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2)
]
# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成
"""


# def find01(list_target):
#     for item in list_target:
#         if item.atk_ratio>6:
#             yield item

class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    ###想转换为看得懂的数据，需要在class SkillData:下添加一个函数__str__
    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2)
]

# re=find01(list_skill)
# for i in re:
#     print(i)
"""
输出结果为：
<__main__.SkillData object at 0x7f09cb9b4eb8>
<__main__.SkillData object at 0x7f09cb9b4ef0>
"""
###在class SkillData:下添加一个函数__str__后的结果：
"""
输出结果为：
技能数据是:102,降龙十八掌,8,5
技能数据是:103,葵花宝典,10,2
"""

# ##生成器表达式
# for i in (item for item in list_skill if item.atk_ratio > 6):
#     print(i)

#######练习６
"""
# 练习2:获取持续时间在4--11之间的所有技能
"""
# def find01(list_target):
#     for item in list_target:
#         if 4 < item.atk_ratio < 11:
#             yield item###返回多个值时，用ｙｉｅｌｄ．且必须用ｆｏｒ形式才能输出为看得懂数据
# re = find01(list_skill)
# for i in re:
#     print(i)

###生成器表达式
# for i in (item for item in list_skill if 4 < item.atk_ratio < 11):
#     print(i)

#######练习７
"""
# 练习3:获取技能编号是102的技能
"""
# def find01(list_target):
#     for item in list_target:
#         if item.id == 102:
#             return item###返回一个值时，用return，且不用ｆｏｒ形式就能输出为看得懂数据，且也不用写成生成器表达式或者列表推导式的形式．
# re=find01(list_skill)
# print(re)

#######练习８
"""
# 练习4:获取技能名称大于4个字并且持续时间小于6的所有技能
"""
# def find01(list_target):
#     for item in list_target:
#         if len(item.name) > 4 and item.duration > 4:
#             yield item
#
# re = find01(list_skill)
# for i in re:
#     print(i)
#
# ###由于条件表达式太长，不用写成生成器表达式的形式．

# for i in (item for item in list_skill if len(item.name) > 4 and item.duration > 4):
#     print(i)

#######练习９
"""
# 需求1:在列表中查找所有偶数
# 需求2:在列表中查找所有大于10的数
# 需求3:在列表中查找所有范围在10--50之间的数
# 1. 使用生成器函数实现以上3个需求
# 2. 体会函数式编程的"封装"
#    将三个函数变化点提取到另外三个函数中.
#    将共性提取到另外一个函数中
# 3. 体会函数式编程的"继承"与"多态"
#    使用变量隔离变化点,在共性函数中调用变量.
# 4. 测试(执行上述功能)
"""
# list01 = [43, 4, 5, 5, 6, 7, 87, 666]
#
# ###生成器表达式
# def find01(list_target):
#     for item in list_target:
#         if item % 2 == 0:
#             yield item
#
#
# def find02(list_target):
#     for item in list_target:
#         if item > 10:
#             yield item
#
#
# def find03(list_target):
#     for item in list_target:
#         if 10 < item < 50:
#             yield item  ###返回多个值时，用ｙｉｅｌｄ．且必须用ｆｏｒ形式才能输出为看得懂数据
#
#
# re = find01(list01)
# for i in re:
#     print(i)

####函数式编程
# def condition1(item):
#     return item % 2 == 0
#
#
# def condition2(item):
#     return item > 10
#
#
# def condition3(item):
#     return 10 < item < 50
#
# print("------------------")
# def fun_find(func_condition):###列表固定
#     for item in list01:
#         if func_condition(item):####此时需要执行，所以func_condition需要参数
#             yield item
#
# for i in fun_find(condition1):####此时只需要将函数condition作为参数传递到fun_find，所以condition不需要参数
#     print(i)
# print("------------------")
# def fun_find(func_condition, list_target):###列表可变
#     for item in list_target:
#         if func_condition(item):
#             yield item
#
# for i in fun_find(condition3, list01):
#     print(i)

#######练习10
"""
# 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
# 需求1:获取攻击比例大于6的所有技能
# 需求2:获取持续时间在4--11之间的所有技能
# 需求3:获取技能名称大于4个字并且持续时间小于6的所有技能
"""
# def condition01(item):
#     return item.atk_ratio > 6
#
# def condition02(item):
#     return 4<item.duration<11
#
# def condition03(item):
#     return len(item.name) > 4 and item.duration < 6
#
# from common.list_helper import *
# generate01=ListHelper.find_all(list_skill,condition01)
# for item in generate01:
#     print(item)
#print("------------------")
# generate02=ListHelper.find_all(list_skill,condition02)
# for item in generate02:
#     print(item)
#print("------------------")
# generate03=ListHelper.find_all(list_skill,condition03)
# for item in generate03:
#     print(item)

#######练习11
"""
# 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
# 案例:查找名称是"葵花宝典"的技能.(单个对象)
#     查找编号是101的技能.(单个对象)
#     查找持续时间大于0的技能.(多个对象)
# 建议:
# 1. 现将所有功能实现
# 2. 封装变化(将变化点单独定义为函数)
#    定义不变的函数
# 3. 将不变的函数转移到list_helper.py中
# 4. 在当前模块测试
"""
#####直接导入ｌｉｓｔ＿ｈｅｌｐｅｒ，用ListHelper输出结果．但是这个的查找值只有一个，不建议用ｙｉｅｌｄ.故重新创建列表助手类
# def condition01(item):
#     return item.name =="葵花宝典"
#
# def condition02(item):
#     return item.id==101
#
# def condition03(item):
#     return item.duration >0
#
# from common.list_helper import *
#
# generate01=ListHelper.find_all(list_skill,condition01)
# for item in generate01:
#     print(item)
#print("------------------")
# generate02=ListHelper.find_all(list_skill,condition02)
# for item in generate02:
#     print(item)
# print("------------------")
# generate03=ListHelper.find_all(list_skill,condition03)
# for item in generate03:
#     print(item)

####下述步骤按题目要求重头开始构造类过程：
# def find01(list_target):
#     for item in list_target:
#         if item.name =="葵花宝典":
#             return item
#
# def find02(list_target):
#     for item in list_target:
#         if item.id==101:
#             return item
#
# def find03(list_target):
#     for item in list_target:
#         if item.duration >0:
#             return item
##封装
# def condition01(item):
#     return item.name =="葵花宝典"
#
# def condition02(item):
#     return item.id==101
#
# def condition03(item):
#     return item.duration >0

# ###继承，移入list_helper.py中，创建类
# def find_single(list_target,fun_condition):
#     for item in list_target:
#         if fun_condition(item):
#             return item
#
# re=find_single(list_skill,condition01)
# print(re)
# print("------------------")
# from common.list_helper import *
# g01=ListHelper1.find_single(list_skill,condition01)
# print(g01)
# print("------------------")
# g02=ListHelper1.find_single(list_skill,condition02)
# print(g02)
# print("------------------")
# g03=ListHelper.find_all(list_skill,condition03)
# for item in g03:
#     print(item)

#######练习12
"""
# 使用lambda实现
# 案例:查找名称是"葵花宝典"的技能.
#     查找编号是101的技能.
#     查找持续时间大于0的技能.
"""
# def condition01(item):
#     return item.name =="葵花宝典"
#
# def condition02(item):
#     return item.id==101
#
# def condition03(item):
#     return item.duration >0

# from common.list_helper import *
# print(ListHelper1.find_single(list_skill,lambda item:item.name =="葵花宝典"))
# print("------------------")

# print(ListHelper1.find_single(list_skill,lambda item:item.id ==101))
# print("------------------")

# for item in ListHelper.find_all(list_skill,lambda item:item.duration
#                                                        >0):####该句中的地二个ｉｔｅｍ表示的是list_skill中的每一个元素，若是不理解，可以看练习１２中的封装和继承部分代码
#     print(item)
#######练习13
"""
# 需求1:计算技能列表中技能名称大于4个字的技能数量.
# 需求2:计算技能列表中技能持续时间小于等于5的技能数量.
# 步骤:
# 实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
# 将不变的函数提取到list_helper.py中
"""
# def find_lambda(list_target,fun_codition):
#     count=0
#     for item in list_target:
#         if fun_codition(item):
#             count+=1
#     return count
#
# from common.list_helper import *
#
# print("------------------")
# g01=ListHelper1.find_lambda(list_skill,lambda item:len(item.name) > 4)
# print(g01)
# print("------------------")
# g02=ListHelper1.find_lambda(list_skill,lambda item:item.duration<=5)
# print(g02)















