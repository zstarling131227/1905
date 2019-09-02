"""
1. 三合一
2. 当前练习独立完成.

5. 阅读python入门到实践第３章和第４章
      程序员的数学第四章
"""

"""
3. 计算列表中最小值(不使用min)．（看内存图day06）

"""
# list1=[]
# while 1:
#     str_input=input("请输入数字：")
#     if str_input=='':
#         break
#     list1.append(int(str_input))
# min_num=list1[0]
# for i in range(len(list1)):
#     if list1[i]<min_num:
#            min_num=list1[i]
# print("最小值是%d"%min_num)

"""
4. 彩票　双色球：
红球:6个，1 -- 33 之间的整数   不能重复#######次数不固定，所以不用for循环
蓝球:1个，1 -- 16 之间的整数
(1) 随机产生一注彩票[6个红球１个蓝球].

(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："
"""
###########１
import random
list1=[]
while len(list1)<6:
    red_num=random.randint(1,34)
    # print(red_num)
    if red_num not in list1:
        list1.append(red_num) 
blue_num=random.randint(1,16)
list1.append(blue_num)
# print(blue_num)
print(list1)
################2
list2=[]
i=1
while len(list2)<6:
    user_red=int(input("请输入第%d红球号码："%i))
    if user_red>34:
        print("号码不在范围内")
        continue################返回到while语句
    elif user_red in list2:
        print("号码已重复")
        continue
    elif len(list2)==6:
        break
    else:
        list2.append(user_red)
        i+=1

while 1:
    user_bule=int(input("请输入蓝球号码："))
    if user_bule<16:
        list2.append(user_bule)
        break
    else:
        print("号码不在范围内")  
print(list2)
sum_num=0
for i in range(7):
    for j in range(7):
        if list1[i]==list2[j]:
            # print("中奖")
            sum_num+=1
print("中奖号码%d个"%sum_num)
