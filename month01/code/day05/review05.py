################练习1

"""
    练习１：
    在控制台中录入，西游记中你喜欢的人物.
    输入空字符串，打印(一行一个)所有人物.
    11:25
"""

# list01=[]
# while 1:
#     figure = input("最喜欢的人物：")
#     list01.append(figure)
#     if figure=="":
#        break
# for i in list01:
#     print(i)

################练习2
"""
# 练习:在控制台中录入，所有学生成绩.
# 输入空字符串，打印(一行一个)所有成绩.
# 打印最高分,打印最低分,打印平均分.
# 11:41
"""
# list01 = []
# while 1:
#     score = input("学生成绩：")
#     if score == "":
#         break
#     list01.append(int(score))  ##########录入时转换类型
# for i in list01:
#     print(i)
# print(max(list01))
# print(min(list01))
# print(sum(list01) / len(list01))

################练习3
"""
# 练习3：
# 在控制台中录入，所有学生姓名.
# 如果姓名重复，则提示"姓名已经存在",不添加到列表中.
# 如果录入空字符串，则倒叙打印所有学生.
"""
#########相比较老师写的，这个删除的是已经输入的重复的元素，而不是新输入的元素。
# list01 = []
# while 1:
#     name = input("学生姓名：")
#     # for i in list01:###########不用多此一举，因为if name in list01:已经可以判断name是否存在在列表中
#     if name in list01:
#             print("姓名已存在")
#             list01.remove(name)
#     if name == "":
#         print(list01[-1:-len(list01)-1:-1])##############倒序取返起始值和结束值一定要判断正确。
#         break
#     list01.append(name)
#############老师讲
# list01 = []
# while 1:
#     name = input("学生姓名：")
#     if name == "":
#         break
#     if name not in list01:
#         list01.append(name)
#     else:
#         print("姓名已存在")
# ####-1  -2  -3
# ####2  1   0(与练习７比较)
# for i in range(-1,-len(list01)-1,-1):
#     print(list01[i])

################练习4（看内存图）
"""
    练习１:
        将列表[54,25,12,42,35,17]中，
        大于30的数字存入另外一个列表.
        并画出内存图.
"""
#############列表1固定元素值
# list1=[54,25,12,42,35,17,789,34,23,10]
# list2=[]
# for i in range(0,len(list1)):
#     if list1[i]>30:
#         list2.append(list1[i])
# print(list2)
#############列表1固定元素个数，但不限定元素值
# count=0
# list1=[]
# list2=[]
# while count<5:
#     num=int(input("数字："))
#     list1.append(num)
#     count+=1
# for i in range(0,len(list1)):
#     if list1[i]>30:
#         list2.append(list1[i])
# print(list2)

#############列表1不固定元素个数，且不限定元素值

# list1=[]
# list2=[]
# while 1:
#     num=input("数字：")
#     if num=="":
#         break
#     list1.append(int(num))
# for i in range(0,len(list1)):
#     if list1[i]>30:
#         list2.append(list1[i])
# print(list2)

################练习5
"""
    练习２：
        在控制台中录入５个数字，
        打印最大值（不适用max）.
"""
#######自己做
# count = 0
# list1 = []
# while count < 5:
#     # num=int(input("数字："))
#     num = int(input("请输入第%d个数字：" % (count + 1)))############学会运用转义字符
#     list1.append(num)
#     count += 1
# max_num = list1[0]
# for i in range(5):
#     if max_num < list1[i]:
#         max_num = list1[i]
# print("最大值为%d" % max_num)

############老师讲
# max_num = 0
# for i in range(5):
#     num = int(input("请输入第%d个数字：" % (i + 1)))  ############学会运用转义字符
#     if max_num < num:
#         max_num = num
# print("最大值为%d" % max_num)

################练习6
"""
# 练习３:
# 在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max).
"""
########自己做（和老师讲一样）
# ###########列表1固定元素值
# list1 = [54, 25, 12, 42, 35, 17, 789, 34, 23, 10]
# max_num = list1[0]
# for i in range(len(list1)):
#     if max_num < list1[i]:
#         max_num = list1[i]
# print("最大值为%d" % max_num)

############更简单的代码写法

# list1 = [54, 25, 12, 42, 35, 17, 789, 34, 23, 10]
# max_num = list1[0]
# for i in list1:
#     if max_num < i:
#         max_num = i
# print("最大值为%d" % max_num)

#############列表1固定元素个数，但不限定元素值
# count = 0
# list1 = []
# while count < 5:
#     num = int(input("请输入第%d个数字：" % (count + 1)))
#     list1.append(num)
#     count += 1
# max_num = list1[0]
# for i in range(len(list1)):
#     if max_num < list1[i]:
#         max_num = list1[i]
# print("最大值为%d" % max_num)


################练习7（看内存图）
"""
# 练习４:在列表中[9, 25, 12, 8]，删除大于10的数字.
# 17:10
"""
##############代码有误，但是可以运行，此时进行调试判断语句为什么出错（remove会覆盖到被删除变量的地址）
# list1 = [54, 25, 12, 42, 35]
# for i in list1:
#     if 20 < i:
#         list1.remove(i)
# print(list1)
##############正确代码，从后往前删除（与练习４比较）
# list1 = [54, 25, 12, 42, 35]
"""
3 2  1 0
-1 -2 -3 -4"""
"""
>>> l=[7,9,0,9,88,9,9]
>>> l2=l[-1:-len(l)-1:-1]
>>> l2
[9, 9, 88, 9, 0, 9, 7]
>>> l2=l[len(l)-1:-1:-1]
>>> l2
[]
>>> for i in range(len(l)-1,-1,-1):
...     print(i)
... 
6
5
4
3
2
1
0
"""
# for i in range(len(list1)-1,-1,-1):############(在理解中～～～～～～～～～～～)
#     if list1[i]>20:
#         list1.remove(list1[i])
# print(list1)

################练习8
"""
# 练习:在控制台中循环输入字符串,如果输入空则停止。
#      最后打印所有内容（拼接后的字符串）.
"""
# list01 = []
# while 1:
#     name = input("请输入字符串：")
#     if name == "":
#         break
#     list01.append(name)
# result="".join(list01)
# print(result)

################练习9
"""
#　练习:英文单词翻转
# "How are you" -->"you are How"
"""
# str01="zcz*fsdf*fsffs*fsf"
# list01=str01.split("*")
# print(list01[::-1])###############正向取反
# list02=" ".join(list01[::-1])
# print(list02)




