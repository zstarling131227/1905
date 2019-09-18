#####练习1
"""
# 练习:当钱不够时，提示"金额不足",
#      钱够时，提示"应找回"
#      调试程序.
"""
# price = float(input("商品单价："))
# count = int(input("数量："))
# total_price = float(input("实收金额："))
# a = total_price - price * count
# if a>=0:
#     print("应找回：", a)
# else:
#     print("金额不足")

#####练习2
"""
    练习:在控制台中获取一个季度(春夏秋冬)，
        显示相应的月份。
        春 --> １月２月３月
        夏 --> ４月５月６月
        秋 --> ７月８月９月
        冬 --> １０月１１月１２月
    14:18
"""
# season= input("输入季度：")
# if season=="春":     #########春要加双引号，否则显示春未定义
#    print("1月2月3月")
# elif season=="夏":
#    print("4月5月6月")
# elif season=="秋":
#    print("7月8月9月")
# elif season=="冬":
#    print("10月11月12月")

# #####练习3
"""
    在控制台中录入一个数字,
    再录入一个运算符(+ - * /)，最后录入一个数字。
    根据运算符，计算两个数字。
    要求:如果运算符，不是加减乘除，则提示"运算符有误"
"""
# num1 = float(input("数字："))
# num2 = float(input("数字："))
# operator = input("运算符：")  ##########input默认的为字符型，无需添加str()
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("运算符有误")

# #####练习4
"""
    在控制台中分别录入４个数字
    打印最大的数字
    5
    2
    9
    1
    将第一个数字记在心里，然后与第二个比较
    如果第二个大于心中的，则心中记录第二个
    然后与第三个比较．．．．
    15:27
"""
# num1 = float(input("数字："))
# num2 = float(input("数字："))
# num3 = float(input("数字："))
# num4 = float(input("数字："))
# max_value=num1
# if max_value<num2:
#     max_value=num2
# if max_value<num3:
#     max_value=num3
# if max_value<num4:
#     max_value=num4
# print(max_value)

# ######练习5
"""
    在控制台中录入一个成绩，
    判断等级（优秀／良好／及格／不及格/输入有误）。
    15:40
"""
# grade = float(input("成绩："))
######方法1
# if 90<=grade<=100:
#     print("优秀")
# elif 80<=grade<90:
#     print("良好")
# elif 60<=grade<80:
#     print("及格")
# elif 0<=grade<60:
#     print("不及格")
# else:
#     print("输入有误")

# #######方法2
# if 0>grade or grade>100:
#     print("输入有误")
# elif 90<=grade:
#     print("优秀")
# elif 80<=grade:
#     print("良好")
# elif 60<=grade:
#     print("及格")
# else:
#     print("不及格")


#######练习6
"""
    在控制台中获取一个月份
    打印天数,或者提示"输入有误".
    1 3 5 7 8 10 12  --> 31天
    4 6 9 11 --> 30天
    2 --> 28天
    16:05
"""
######方法1
# month = int(input("月份："))
# if month==2:
#     print("28天")
# elif month==4 or month==6 or month==9 or month==11:
#     print("30天")
# elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print("31天")
# else:
#     print("输入有误")

# ########方法2
# month = input("月份：")##############若是未定义数据的类型，则将后面的数据带双引号表示字符串。
# if month=="2":
#     print("28天")
# elif month=="4" or month=="6" or month=="9" or month=="11":
#     print("30天")
# elif month=="1" or month=="3" or month=="5" or month=="7" or month=="8" or month=="10" or month=="12":
#     print("31天")
# else:
#     print("输入有误")

# ########方法3
# month = input("月份：")
# if month<"1" or month>"12":##############此处表示的是字符串的大小比较， 而不是数值大小的比较，故结果出错。修改方式为将month定义为整形，去掉双引号。
#     print("输入有误")
# elif month=="2":
#     print("28天")
# elif month=="4" or month=="6" or month=="9" or month=="11":
#     print("30天")
# else:
#     print("31天")

# #######练习7
"""
在控制台中获取一个整数，
如果是偶数为变量state赋值"偶数",否则赋值"奇数"
"""
# #######方法1
# num = None
# num = "偶数" if int(input("整数：")) % 2 == 0 else "奇数"
# print(num)
# #########方法2
# num = "奇数" if int(input("整数：")) % 2  else "偶数"  ############bool(true)=1,而int(input("整数：")) % 2 ==1 表示奇数。
# print(num)

# #######练习8
"""
    在控制台中录入一个年份，
    如果是闰年，给变量day赋值29，否则赋值28.
    16:40
"""
# while True:
#     ######方法1
#     year = int(input("年份："))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         day=29
#     else:
#        day=28
#     print(day)
#     #######方法2
#     day=29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#     print(day)
#
#     #######方法3
#     day=29 if not year % 4 and year % 100 or not year % 400 else 28
#     print(day)
#     #######方法4
#     if not year % 4  and year % 100 or not year % 400  :
#         day=29
#     else:
#        day=28
#     print(day)
#     if year==0:
#         break

# ####练习9
"""
    练习:使下列代码循环执行，按e键退出。
    调试程序
"""
# while True:
#     season= input("输入季度：")
#     if season=="春":     #########春要加双引号，否则显示春未定义
#        print("1月2月3月")
#     elif season=="夏":
#        print("4月5月6月")
#     elif season=="秋":
#        print("7月8月9月")
#     elif season=="冬":
#        print("10月11月12月")
#     elif season=="e":
#         break

####练习10
"""
    练习:在控制台中输出0 1 2 3 4 5
    练习:在控制台中输出2 3 4 5 6 7
    练习:在控制台中输出0 2 4 6
"""
################方法1   print 和count的位置影响输出的结果
# count=-1
# while count <5:
#     count +=1
#     print(count)

# count=1
# while count <7:
#     count +=1
#     print(count)

# count=-2
# while count <5:
#     count +=2
#     print(count)

# ###########方法2
# count=0
# while count <6:
#     print(count)
#     count +=1

# count=2
# while count <8:
#     print(count)
#     count +=1

# count=0
# while count <7:
#     print(count)
#     count +=2