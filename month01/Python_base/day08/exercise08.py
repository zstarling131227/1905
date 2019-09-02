"""
day08
1. 三合一
2. 当天练习独立完成
6. 玩2048游戏(了解游戏规则).
8. 阅读:python入门到实践第8章
"""

"""
3. 自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
    字符串："　校　训：自　强不息、厚德载物。　　"
    查找空格的数量
    删除字符串前后空格
    删除字符串所有空格
    查找"载物"的位置
    判断字符串是否以"校训"开头.
"""
str01=" 校 训：自 强不息、厚德载物。  "
############以下生成新的字符串，不是修改str01,因为字符串是不可变的。
# print(str01.count(" "))
# str01.lstrip().rstrip()
# print(str01.lstrip())
# print(str01.rstrip())
# print(str01.strip())
# print(str01.replace(" ",""))
# print(str01.index("载物"))
# print(str01.startswith("校训"))

"""
# 4. 定义函数，计算指定范围内的素数
#     for i in range(start,end):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
"""
# def is_prime(number):
#     """
#     判断是否是素数
#     :param number: 判断值
#     :return: True或False
#     """
#     for j in range(2, number):
#         if number % j == 0:
#             return False
#     return  True
# def prime_number(start,end):
#     """
#     获取范围内的素数
#     :param start: 起始值（包含）
#     :param end: 结束值（不包含）
#     :return: 所有素数的列表
#     """
#     # list01=[]
#     # for number in range(start,end):
#     #    if is_prime(number):
#     #        list01.append(number)
#     ###上述方法为复杂方法
#     return [number for number in range(start,end) if is_prime(number) ]
#
# result=prime_number(2,19)
# print(result)

#######下述方法不建议
# def prime_number(start,end):
#     list01=[]
#     for i in range(start,end):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             list01.append(i)
#     return list01
#
# result=prime_number(2,19)
# print(result)

#######下述方法为快捷键法
def prime_number(start,end):
    list01=[]
    for i in range(start,end):
        is_prime(i)#########Ctrl+alt+m键快速生成函数，ctrl+左键，查看函数信息
    return list01

def is_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


result=prime_number(2,19)
print(result)

"""
5. 群讨论：is  与 == 的区别
a = [1,2]
b = [1,2]
print(a is b)
print(a == b)
"""
"""
is 与 == 区别：

is 用于判断两个变量引用对象是否为同一个，
== 用于判断引用变量的值是否相等。
"""
"""
a = [1, 2, 3]
b = a
b is a ###True
b == a ##True
b = a[:]
b is a ###False
b == a ###True

"""
"""
7. 重构 shopping.py 程序
   不改变原有功能，修改程序代码。
"""
# ####      位置参数　　星号元组　命名关键字　双星号字典
# def fun07(a=0,b=0,*args,c,d,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#     print(kwargs)
#
# fun07(12,12,5,6,7,89,c=5,d=7,e=9,t=7)
# ####      位置参数　　星号元组　命名关键字　双星号字典
# def fun07(a=0,b=0,*args,c=0,d=0,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#     print(kwargs)
# ###若关键字给默认值，则把关键字实参可以补不写
# fun07(12,12,5,6,7,89,e=9,t=7)

#### 　命名关键字　双星号字典
# def fun08(*args,**kwargs):
#     print(args)
#     print(kwargs)
# fun08(1,2,3,a=4,b=5)
# fun08(1,2,3,4,5)
# fun08(a=4,b=5)

