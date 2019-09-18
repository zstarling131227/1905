########作业
"""
3.在控制台中获取月份,显示季度,或者提示月份错误.
"""
##########方法1
month = int(input("月份："))
if month==1 or month==2 or month==3:
    print("春")
elif month==4 or month==5 or month==6:
    print("夏")
elif month==7 or month==8 or month==9:
    print("秋")
elif month==10 or month==11 or month==12:
    print("冬")
else:
    print("输入有误")
###########方法2
month = int(input("月份："))
if month<1 or month>12 :
    print("输入有误")
elif month >=10:
    print("冬")
elif month >=7:
    print("秋")
elif month>=4:
    print("夏")
else:
    print("春")
    """
4.在控制台中获取年龄，
如果小于０岁，打印输入有误
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁～150岁，就打印一条消息，指出他是老年人。
150岁以上，打印"那不可能"
"""
age=int(input("请输入年龄："))
if age<0:
    print("输入有误")
elif age<2:
    print("婴儿")
elif age<13:
    print("儿童")
elif age<20:
    print("青少年")
elif age<65:
    print("成年人")
elif age<150:
    print("老年人")
else:
    print("那不可能")
"""
5.根据身高体重,参照BMI,返回身体状况.
 BMI:用体重千克数除以身高米数的平方得出的数字
 中国参考标准
 体重过低BMI<18.5
 正常范围18.5≤BMI<24
 超重24≤BMI<28
 I度肥胖28≤BMI<30
 II度肥胖30≤BMI<40
 Ⅲ度肥胖BMI≥40.0
"""
weight=float(input("请输入体重："))
height=float(input("请输入身高："))
BMI=weight/height**2
if BMI<18.5:
    print("体重过低")
elif BMI<24:
    print("正常范围")
elif BMI<28:
    print("超重")
elif BMI<30:
    print("I度肥胖")
elif BMI<40:
    print("II度肥胖")
else:
    print("Ⅲ度肥胖")









