"""
汇率转换器
"""
# # 1. 获取数据
# str_usd = input("请输入美元：")
# int_usd = int(str_usd)
# # 2. 逻辑处理
# result = int_usd * 6.9
# # 3. 显示结果
# print(result)
# print()
# 程序是改出来的
# 英文不好用有道
# 程序不是自上而下编写的
# 一行代码往往是从右向左写的


# #########练习1 交换变量值
# """
# # 在控制台中获取两个变量，然后交换数据，最后显示结果.
# # “请输入第一个变量：”
# # “请输入第二个变量：”
# #      交换
# # “第一个变量是：”
# # “第二个变量是：”
# """

# a = input("请输入第一个变量：")
# b = input("请输入第一个变量：")
#
# ##########方法1
# c = a  ####c是用来临时的存储值
# a = b
# b = c
# ####方法2
# a,b=b,a
#
# print("变量a是：" + a)
# print("变量b是：" + b)

######练习2
# """
# # 在控制台中，录入一个商品单价。25
# # 再录入一个数量  2
# # 最后获取金额，60 计算应该找回多少钱。60 - 25*2
# # 14:45
# """
# price = float(input("商品单价："))
# count = float(input("数量："))
# totalprice = float(input("实收金额："))
# a = totalprice - price * count
# # print("应找回：",totalprice-price*count)
# print("应找回：", a)
# print("应找回：" + a)###########字符型不能和数整形用加号“+”连接
# print("应找回：" + str(a))###########字符型和数字用加号“+”连接时，应该将数值型转换为字符串型

# #######练习3
# """
# #      在控制台中获取分钟
# # 　　　　再获取小时
# # 　　　　再获取天
# #       计算总秒数
# # 15:35
# """
# minute=int(input("分:"))
# hour=int(input("时:"))
# day=int(input("天:"))
# second=minute*60+hour*60**2+day*24*60**2
# print("总秒数：",second)

# #############练习4
# """
#     古代的秤一斤是１６两  33  二斤　　一两
#     练习：在控制台中获取两，计算是几斤零几两。
#     　　　显示几斤零几两
#     15:43
# """
# data=float(input("请输入一个数:"))
# jin=data//16
# liang=data%16
# print(jin,"斤"0,liang,"两")

# #######练习5
# """
# # 在控制台中录入距离，时间，初速度，计算加速度。
# # 匀变速直线运动的位移与时间公式：
# # 加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方
# """
# initial_velocity=int(input("初速度是（米每秒）："))
# time=int(input("时间是（秒）："))
# distance=int(input("位移是（米）："))
# accelerated_speed=(distance-initial_velocity*time)*2/time**2
# print("加速度是："+str(accelerated_speed)+"m/s^2")

# ########练习6
# """
# # 在控制台中录入一个四位整数：1234
# # 计算每位相加和。　　１＋２＋３＋４
# # 显示结果。10
# """
# ####方法1
# interger=int(input("请输入一个四位数整数："))
# gewei=interger%10
# shiwei=(interger%100)//10
# baiwei=(interger%1000)//100
# qianwei=interger//1000
# sum=gewei+shiwei+baiwei+qianwei
# print("求和得：",sum)
# ####方法2
# interger = int(input("请输入一个四位数整数："))
# gewei = interger % 10
# shiwei = interger // 10 % 10
# baiwei = interger // 100 % 10
# qianwei = interger // 1000
# sum = gewei + shiwei + baiwei + qianwei
# print("求和得：", sum)
# #####方法3
# interger = int(input("请输入一个四位数整数："))
# sum = interger % 10    ######################定义一个sum初始值
# sum += interger // 10 % 10
# sum += interger // 100 % 10
# sum += interger // 1000
# print("求和得：", sum)

############练习8
# """
# 判断年份是否为闰年。
# """
# interger = int(input("请输入一个年份："))
# print(bool((interger % 4 == 0 and interger % 100 != 0) or interger % 400 == 0))
# if interger % 4 == 0 and interger % 100 != 0 or interger % 400 == 0:###############不加括号也可以，and和or从左到右依次执行
#     print("是闰年")
# else:
#     print("是平年")
