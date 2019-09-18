"""
3.  按照以下格式，输出变量name = "悟空",age = 800,score = 99.5
     我叫xx,年龄是xx,成绩是xx。
"""
url = "我叫%s,年龄是%d,成绩是%.1f" % ("悟空", 800, 99.5)
print(url)
"""
4.　在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****

       6
       ******
       *    *
       *    *
       *    *
       *    *
       ******
"""
#####
num = int(input("数字："))
if num<=1:
    print("输入的数字必须大于2")
print(num * "*")
for i in range(num - 2):
    print("*" + (num - 2) * " " + "*")
print(num * "*")
"""
5.在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上
"""
###
str_num1 = input("输入字符串：")
if str_num1 == str_num1[::-1]:
    print("是回文")
else:
    print("不是回文")
"""（看内存图day05）
# 6. (扩展)一个小球从１００ｍ的高度落下
#     　　每次弹回原高度的一半．
#     　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
#             总共走了多少米
"""
##
count=0  ######弹起来多少次
height = 100
sum_height=0
while height>0.01:
    height /= 2
    # print(height)
    count+=1
    sum_height+=height*2
    # print(sum_height)
print(count)
print(sum_height+100)






