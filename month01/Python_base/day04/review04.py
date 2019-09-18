#############练习1
"""
    练习1:在控制台中，获取一个开始值，一个结束值。
        　将中间的数字打印出来。
        例如：开始值3  结束值10
              打印4  5  6  7  8  9
    9:43
"""
# begin_num = int(input("数字1："))
# end_num = int(input("数字2："))
# while begin_num < end_num - 1:
#     begin_num += 1
#     print(begin_num)

#############练习2
"""
# 练习:一张纸的厚度是0.01毫米，
#  请计算对折多少次，超过珠穆朗玛峰8844.43米。
# 10:30
"""
# thickness=0.01
# i=0
# while thickness<8844430:
#     thickness*=2
#     i+=1
#     print(thickness)
# print(i)
###########单位换算方式
# thickness=0.00001
# i=0
# while thickness<8844.430:
#     thickness*=2
#     i+=1
# print(i)

#############练习3
"""
    练习:猜数字游戏
    游戏运行产生一个１－－１００之间的随机数。
    让玩家重复猜测，直到猜对为止。
    提示:大了
    　　　小了
    　　　　猜对了，总共猜了多少次
    10:47
"""
# import random
# random_randint = random.randint(1, 100)
# # print(random_randint)
# count = 0
# while True:
#     num = int(input("数字："))
#     count += 1
#     if num > random_randint:
#         print("大了")
#     elif num < random_randint:
#         print("小了")
#     else:
#         print("猜对了,总共猜了",count,"次")
#         break
# print(count)

#############练习4
"""
    猜数字2.0:
        最多猜３次，如果猜对提示"猜对了，总共猜了?次"
        如果超过次数，提示"游戏结束".
    练习:exercise04.py
"""
# random_randint = random.randint(1, 100)
# # print(random_randint)
# count = 0
# while count<3:
#     ######3次以内的循环
#     num = int(input("数字："))
#     count += 1
#     if num > random_randint:
#         print("大了")
#     elif num < random_randint:
#         print("小了")
#     else:
#         print("猜对了,总共猜了",count,"次")
#         break####退出循环体，不执行else
# else:
#     ##########3次以外的循环
#     print("游戏结束")

#############练习5（同练习9）
"""
# 练习:循环根据成绩判断等级,如果录入空字符串则退出程序.
# 如果成绩录入错误次数达到３．则退出成绩并提示"成绩错误过多"
"""
###############错误代码
"""空字符串的只能与字符型比较，不能与数值型比较，否则会报错"""
# count=0
# while count<2:
#     count +=1
#     grade = int(input("成绩："))############输入空格会显示错误
#     if 0>grade or grade>100:
#         print("输入有误")
#     elif 90<=grade:
#         print("优秀")
#     elif 80<=grade:
#         print("良好")
#     elif 60<=grade:
#         print("及格")
#     elif grade<60:
#         print("不及格")
#     elif grade=="":
#         break
# else:
#     print("成绩错误过多")
"""空字符串的只能与字符型比较，不能与数值型比较，否则会报错"""
# ###############正确代码
# count=0
# while count<3:
#     str_grade = input("成绩：")
#     if str_grade=="":
#         break############不会执行else语句
#     grade = int (str_grade)
#     if 0>grade or grade>100:
#         print("输入有误")
#         count +=1##############显示3次输入有误的时候退出循环
#     elif 90<=grade:
#         print("优秀")
#     elif 80<=grade:
#         print("良好")
#     elif 60<=grade:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("成绩错误过多")

#############练习6
"""
# 练习1:累加1--100的和  1+2+3+..+100
# 练习2:累加1--100之间偶数和  2+4+6+8+...+100
        累加1--100之间奇数和 
# 练习3:累加10--36之间的和
"""
#用于存储累加和的变量
# sum =0
# for i in range(0,101):
#     # i+=1##############i在for中自动循环，不需要再手动循环，否则i会多1,结果输出为5050.
#     sum = sum + i  ##########相当于sum+=i
# print(sum)
####奇数求和
# sum =0
# for i in range(1,101,2):
#     sum+=i
# print(sum)
# #######偶数求和
# sum =0
# for i in range(0,101,2):
#     sum+=i
# print(sum)
#
# sum =0
# for i in range(10,36):
#     sum = sum + i
# print(sum)


#############练习7
"""
    练习:随机加法考试
      随机产生两个数字(1--10),
      在控制台中获取两个数相加的结果
      如果用户输入正确得１０分
    　总共３道题，最后输出得分.
    　例如:"请输入8+3=?"   10   不得分
    　　　　"请输入4+3=?"   7   得10分
    　　　　"请输入4+4=?"   8   得10分
          　”总分是20“
    　14:15

"""
import random

# #count = 0
# score=0
# for i in range(0,3):
#     #count+=1   ##########for循环不需要再手动遍历
#     random_num1 = random.randint(1, 10)
#     random_num2 = random.randint(1, 10)
#     print(random_num1,random_num2)
#     sum=random_num1+random_num2
#     user_sum=int(input("请输入结果："))
#     if sum==user_sum:
#         score+=10
#     else:
#         score=0
# print("总分是",score)

##########老师讲（需要补充）
# score=0
# for i in range(0,3):
#     random_num1 = random.randint(1, 10)
#     random_num2 = random.randint(1, 10)
#     sum=random_num1+random_num2
#     user_sum=int(input("请输入结果："))
#     if sum==user_sum:
#         score+=10
# print("总分是",score)

#############练习7
"""
# 在控制台中获取一个整数，判断是否为素数。
# 素数:只能被１和自身整除的正数.
# 思路：排除法,使用２到当前数字之间的正数判断，如果存在被整除，则不是素数.
#  判断9：
#     能否被2　--  8 之间的数字整除,其中3可以，所以不是素数.
#  判断８:
#     能否被2　--  7 之间的数字整除,其中2可以，所以不是素数.
#  判断7:
#     能否被2　--  6 之间的数字整除,其中没有，所以是素数.
# 2 3 5  7  11  13  15 ....

# ---------思考过程----------------
# 假设判断11
# 　　　2  -- 10 之间的数字整除

# if 11 % 2 == 0:
# print("不是素数")

# if 11 % 3 == 0:
# print("不是素数")

# if 11 % 4 == 0:
# print("不是素数")
"""
################自己做
# while 1:#########针对输入的数而言的循坏，避免每次输入数据时都要重新点击执行键
# count = 0
# num = int(input("请输入整数："))
# for i in range(2, num):##########备注：没有判断２以下的数字判断2 到number之间的数字，能否整除number.
#     if num % i == 0:
#         count += 1
# if count == 0:
#     print("是素数")
# else:
#     print("不是素数")
# ###           #########两者的循坏次数相同，且会将i从从始至终遍历全部
# if count != 0:
#     print("不是素数")
# else:
#     print("是素数")

#############老师讲（相比于方法一循坏次数少）
# num = int(input("请输入整数："))
# for i in range(2, num):
#     if num % i == 0:
#         print("不是素数")
#         break#################如果发现已满足条件的数字，则不在判断到后面的了
# else:
#     print("是素数")

#############练习8
"""
# 累加10-50之间个位不是2,5,9的整数.
"""
###########方法1
# sum_num=0
# for i in range(10,51):
#     if i%10==2 or i%10==5 or i%10==9:
#         continue  #############满足if后的条件时执行continue，但是不满足题目中的条件。
#     sum_num+=i
# print(sum_num)
# ###########方法2
# sum_num=0
# for i in range(10,51):
#     if i%10!=2 and i%10!=5 and i%10!=9:
#         sum_num+=i
# print(sum_num)

#############练习9（补充输入空字符时的特点)
"""
# 练习1:在控制台中，获取一个字符串.
# 打印每个字符的编码值
# 练习2:在控制台中，重复录入一个编码值，然后打印字符.
#      如果输入空字符串，则退出程序.
"""
###练习
# str_num1=input("输入字符串：")
# for i in str_num1:
#     print(ord(i))
####练习
# while 1:
#     str_num2=input("输入编码值：")
#     if str_num2=="":
"""空字符串的只能与字符型比较，
        不能与数值型比较，否则会报错"""
#         break
#     print(chr(int(str_num2)))


#############练习10
"""
# 练习:在控制台中获取一个字符串
# 打印第一个字符
# 打印最后一个字符
# 打印倒数第三个字符
# 打印前两个字符
# 倒序打印字符
# 如果字符串长度是奇数，则打印中间字符.
"""
# str_num1=input("输入字符串：")
# print(str_num1[0])
# print(str_num1[-1])
# print(str_num1[-3])
# print(str_num1[:2])
# print(str_num1[::-1])
# if len(str_num1)%2==1:
#     print(str_num1[int((len(str_num1)-1)/2)])#########也可以用地板除int(len(str_num1)//2)












