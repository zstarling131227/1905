"""
    函数参数
        形式参数

"""
#1.缺省（默认）参数：如果实参不提供，可以使用默认值．
# def fun01(a=0,b=0,c=0,d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# #关键字实参+缺省形参：调用者可以随意传递参数．
# fun01(b=1,d=2)
# fun01(1,2)###此时按位置

##练习：定义函数，根据小时，分钟，秒，计算总秒数．
#要求：

# 2.位置参数
# def fun01(a=0,b=0,c=0,d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)

#3.型号元组形参：*将所有实参合并为一个元组
#作用：让实参个数无限
# def fun03(*args):
#     print(args)
# fun03()#()
# fun03(1)#(1,)
# fun03(1,"2")#(1,'2')

#练习：定义函数，让所有数值相加的函数

#4.命名关键字形参:在星号元组形参以后的位置形参
#目的：要求实参必须使用关键字实参
# def fun04(a,*args,b):####a表示位置形参，*args表示元组形参，ｂ表示关键字形参
#     print(a)
#     print(args)
#     print(b)
#
# fun04(1,b=2)####args未赋值，输出结果为()
# fun04(1,2,3,4,b=2)
#
# def fun05(*,a,b):
#     print(a)
#     print(b)
#
# fun05(a=1,b=2)
#

#5.双星号字典形参：**的目的是将实参合并为字典
# 实参可以传递数量无限的关键字实参
# def fun06(**kwargs):
#     print(kwargs)
# fun06(a=1,b=2)#####输入时必须输入关键字a,b

# def fun07(a,b,*args,c,d,**kwargs):
#     pass