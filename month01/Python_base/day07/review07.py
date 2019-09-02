###########练习1
"""
练习:["无忌","赵敏","周芷若"]
#   ->{"无忌":2,"赵敏":2,"周芷若":3}
"""
# list01=["无极","张惠妹","这种人"]
# dict01={}
# for i in list01:
#     dict01[i]=len(i)
#     # print(dict01)
# dict02={i:len(i) for i in list01}
# print(dict02)

###########练习2
"""
# 练习:["无忌","赵敏","周芷若"]  [101,102,103]
#  {"无忌":101,"赵敏":102,"周芷若":103}
"""
# list01=["无极","张惠妹","这种人"]
# list02=[101,102,103]
# dict01={}
# for i in range(len(list01)):
#     dict01[list01[i]]=list02[i]
# print(dict01)

###########练习3
"""
# 练习: 在控制台中循环录入字符串，输入空字符停止.
#       打印所有不重复的文字
"""
# set01 = set()
# while 1:
#     str = input("请输入字符：")
#     if str == "":
#         break
#     set01.add(str)
# print(set01)

###########练习4
"""
练习: 经理：曹操,刘备,孙权
      技术：曹操,刘备,张飞,关羽
请计算：
     (1)是经理也是技术的有谁？
     (2)是经理，不是技术的有谁?
     (3)是技术，不是经理的有谁?
     (4)张飞是经理吗?
     (5)身兼一职的都有谁?
     (6)经理和技术总共有都少人?
"""
# message = {"曹操", "刘备", "孙权"}
# technology = {"曹操", "刘备", "张飞", "关羽"}
# print(message & technology)###交集
# print(message - technology)###补集：返回只属于其中之一的元素
# print(technology - message)
# print("张飞" in message)
# print(message ^ technology)###补集：返回不同的的元素
# print(len(message | technology))###并集

###########练习5
"""
[3,80,45,5,7,1]
目标:列表中所有元素两两比较
思想:
　取出第一个元素,与后面元素进行比较.
　取出第二个元素,与后面元素进行比较.
　取出第三个元素,与后面元素进行比较.
  ...
  取出倒数第二个元素,与后面元素进行比较.
  如果取出的元素大于(>)后面的元素,
      则交换
14:47
list01 = [3, 80, 45, 5, 7, 1]

取出第一个元素,与后面元素进行比较
list01[0]  list01[1]
list01[0]  list01[2]
list01[0]  list01[3]
for c in range(1,len(list01)):
    # list01[0]  list01[c]
    pass
取出第二个元素,与后面元素进行比较
for c in range(2,len(list01)):
    # list01[1]  list01[c]
    pass
取出第三个元素,与后面元素进行比较
for c in range(3,len(list01)):
    # list01[2]  list01[c]
    pass
15:22 上课
"""
"""
###交换元素
c = list01[i]
list01[i] = list01[j]
list01[j] = c
可以直接写成
list01[i],list01[j]= list01[j],list01[i]
"""
# ###########降序
# list01 = [3, 80, 45, 5, 7, 1]
# for i in range(len(list01)):
#     for j in range(i, len(list01)):
#         if list01[i] < list01[j]:
#             c = list01[i]
#             list01[i] = list01[j]
#             list01[j] = c
#     #         print(list01)
#     # print(list01)
# print(list01)

# ###########升序
# list01 = [3, 80, 45, 5, 7, 1]
# for i in range(len(list01)):
#     for j in range(i, len(list01)):
#         if list01[i] > list01[j]:
#             list01[i], list01[j] = list01[j], list01[i]
#     #       print(list01)
#     # print(list01)
# print(list01)

###########练习6
"""
    练习:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
    15:35
"""
###自己做
# list01 = [3, 80, 45, 5, 80, 1]
# for i in range(len(list01)):
#     for j in range(len(list01)):
#         if list01[i] == list01[j] and i!=j:
#             print(list01[i])

###########练习7
"""
练习1:打印第二行第三个元素  15:56
练习2:打印第三行每个元素
练习3:打印第一列每个元素
"""
# list1=[]
# for i in range(1,17):
#     list1.append(i)
# print(list1)
#
# list01=[
#     [1, 2, 3, 4],
#     [ 5, 6, 7, 8],
#     [ 9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# print(list01[1][2])
# print(list01[2][:])
# for i in range(4):
#     print(list01[i][0])

###########练习8
"""
练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
  第一列变成第一行
  第二列变成第二行
  第三列变成第三行

list01=[
    [1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]
"""
# list02=[]
# for i in range(4):
#     line=[]
#     list02.append(line)
#     for j in range(4):
#         line.append(list01[j][i])
# print(list02)

# #####简单写法，且数字不固定
# list02=[]
# for i in range(len(list01[0])):
#     list02.append([])
#     for j in range(len(list01)):
#         list02[i].append(list01[j][i])
#
# print(list02)
##########练习9
"""
练习:列表的全排列
[“香蕉”,"苹果","哈密瓜"]
[“可乐”,"牛奶"]
"""
# list01=["香蕉","苹果","哈密瓜"]
# list02=["可乐","牛奶"]
# list03=[]
# for i in list01:
#     for j in list02:
#         list03.append(i+j)
# print(list03)
#
# list04=[i+j for i in list01 for j in list02]
# print(list04)

##########练习10
"""
练习:将下列代码，定义到函数中，再调用一次.
"""
####固定函数
# def print_rectangle():
#     for i in range(3):
#         for j in range(4):
#             print("*",end="")
#         print()
# print_rectangle()
######可变函数
# def print_rectangle1(r_count,c_count,char):
#     """
#        打印矩阵
#        :param r_count:行数
#        :param c_count:列数
#        :param char:字符
#     """
#     for i in range(r_count):
#         for j in range(c_count):
#             print(char,end="")
#         print()
# print_rectangle1(4,3,"&")
##########练习11
"""
练习:定义在控制台中打印一维列表的函数.
例如：[1,2,3]-->1 2 3  每个元素一行
"""
# def print_list():
#     list=[1,2,3]
#     for i in list:
#         print(i)
# print_list()
# #########可变列表
# def row(list_target):
#     """
#     打印列表
#     :param list_target: 目标列表
#     """
#     for i in list_target:
#         print(i)
#
# row([1,23,4,54,4])


