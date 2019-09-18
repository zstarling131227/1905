###练习１
# 练习1：使用迭代器原理，遍历元组.
# ("铁扇公主","铁锤公主",“扳手王子”)
##元组
# list01=("铁杉公主","贴士公主","扳手王子")
# str01=list01.__iter__()
# while True:
#     try:
#         item=str01.__next__()
#         print(item)
#     except:
#         break

#####练习２
# 练习2:不使用for，获取字典所有数据。
#  {"铁扇公主":101,"铁锤公主":102,“扳手王子”:103}
# 10:40
##字典
# dict01={"铁杉公主":101,"贴士公主":102,"扳手王子":103}
# str02=dict01.__iter__()
# while True:
#     try:
#         item=str02.__next__()
#         print(item)
#         print(dict01[item])
#     except:
#         break

#####练习３
###重复步骤[{}]
# dict01={"铁杉公主":101,"贴士公主":102,"扳手王子":103}
# list02=[]
# list02.append(dict01)
# print(list02)
# for j in list02[0]:
#     print(j)
#     print(list02[0][j])

# str02=list02.__iter__()
# item1=str02.__next__()
# str03=item1.__iter__()
# while True:
#     try:
#         item=str03.__next__()
#         print(item)
#         print(list02[0][item])
#     except:
#         break

#####练习４　

# 练习：图形管理器记录多个图形
#      迭代图形管理器对象
class Graphic:
    pass


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的数据。
        return GraphicIterator(self.__graphics)


class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了，则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration

        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())


# for item in manager:
#     print(item)

# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

#####练习5　

# 练习：员工管理器记录多个图形
#      迭代图形管理器对象
class Employee:
    pass


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employees(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
        else:
            raise ValueError

    def __iter__(self):
        return EmployeeIterator(self.__employees)

    def get_total_wage(self):
        total_wage = 0
        for item in self.__employees:
            total_wage += item.caculate_wage()
        return total_wage


class EmployeeIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了，则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration

        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


# employee1=EmployeeManager()
# employee1.add_employees(Employee())
#
# iterator = employee1.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


####练习６
"""
    练习：定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""
class Myrange:
    def __init__(self, stop__value):
        self.stop__value = stop__value

    def __iter__(self):
        return MyrangeIterator(self.stop__value)


class MyrangeIterator:
    def __init__(self, end_value):
        self.__end_value = end_value
        self.__index = 0

    def __next__(self):
        if self.__index == self.__end_value:
            raise StopIteration

        temp = self.__index
        self.__index += 1
        return temp


# for item in Myrange(10):
#     print(item)


#####练习7　
"""
# 练习: 将迭代器版本的图形管理器改为yield实现.
# exercise03.py -->exercise06.py
# 15: 30
"""
class Graphic:
    pass


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的数据。

        # for item in self.__graphics:
        #     yield item

        for item in range(len(self.__graphics)):
            yield self.__graphics[item]
        """
        输出结果为：
        < __main__.Graphic object at 0x7f09a9680f60 >
        < __main__.Graphic object at 0x7f09a9680f98 >
        """

        # number = 0
        # while number < len(self.__graphics) - 1:
        #     yield number
        #     number += 1
        """
              输出结果为：１，２，３，４，５，……，
       　"""


"""

class GraphicIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了，则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration

        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp
"""
manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

#####写法１
# for item in manager:
#     print(item)

#####写法２　
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break

#####练习８
"""
# 练习1:从列表[4,5,566,7,8,10]中选出所有偶数
# -- 结果存入另外一个列表中
# -- 使用生成器实现
"""
list01 = [1, 12, 545, 44, 55, 4, 445, 45, 48, 5]

###方法１(问题)
# def even01(target_list):
#     list02 = []
#     for item in target_list:
#         if item % 2 == 0:
#             list02.append(item)
#     return list02

# print(even01(list01))

# g03 = even01(list01)
# print(g03)

"""
输出结果都为：[12, 44, 4, 48]
"""

###方法２
# def even(target_list):
#     list02 = []
#     for item in target_list:
#         if item % 2 == 0:
#             list02.append(item)
#             yield list02

# print(even(list01))
"""
输出结果为：<generator object even at 0x7f8f98b080f8>
# 必须经过调用才能输出结果。
"""
# g02=even(list01)
# for i in g02:
#     print(i)
"""
输出结果为：
[12]
[12, 44]
[12, 44, 4]
[12, 44, 4, 48]
"""
###方法２的简化版
# def even(target_list):
#     for item in target_list:
#         if item % 2 == 0:
#             yield item

# print(even(list01))

"""
输出结果为：<generator object even at 0x7f8f98b080f8>
# 必须经过调用才能输出结果。
"""

# g01=even(list01)
# for i in g01:
#     print(i)
"""
输出结果为：
12
44
4
48
"""
