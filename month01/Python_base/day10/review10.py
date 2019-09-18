#####练习１
"""
# 练习：参照day06/exercise07.py
1. 创建学生类
    -- 数据：姓名,年龄,成绩，性别
　　 -- 行为：在控制台中打印个人信息的方法
2. 在控制台中循环录入学生信息，如果名称是空字符,退出录入。
3. 在控制台中输出每个学生信息(调用打印学生类的打印方法)
4.　打印第一个学生信息
# 11:02
"""
class Student():
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_info1(self):  ##（问）
        return ("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))

    def print_info2(self):  ##（问）
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))
        # print((self.name, self.age, self.score, self.sex) % "%s的年龄是%d,成绩是%d,性别是%s")
        # print(name, age,score,sex)#####print_info没有参数，print（）内不能直接写成这种形式

    # def print_info(self,name, age, score, sex):
    #     print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))
    #     print(str(name) + "的年龄是" +str( age) + ",成绩是" + str(score) + ",性别是" + str(sex))
    #     print(name, age, score, sex)


# list_student_info = []
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))
#     sex = input("请输入性别：")
#     student_info = Student(name, age, score, sex)
#     list_student_info.append(student_info)
# for student_info in list_student_info:
#     student_info.print_info()

#####练习2
"""
# 练习1:定义函数,在list01中查找name是"苏大强"的对象.
#      将名称与年龄打印在控制台中
(看 day10　的内存图)
"""
list01 = [
    Student("郝敏", 28, 100, "女"),
    Student("苏大强", 78, 60, "女"),
    Student("名誉", 58, 80, "男"),
    Student("张惠妹", 28, 90, "男"),
    Student("预计", 26, 99, "女")
]


def find01():
    for item in list01:
        if item.name == "苏大强":
            return item
    ##如果没有找到苏大强，则返回空。而函数默认值为空，所以ｒｅｔｕｒｎ可以不写
    return None


# stu=find01()
# print(stu.name,stu.age)
# print(str(stu.name)+str(stu.age))

###不用定义函数时查找数据（此时苏大强的索引容易找到）
# print(list01[1].name)
# print(list01[1].age)

#####练习３
"""
# 练习2:定义函数,在list01中查找所有女同学.
#      将名称与性别打印在控制台中
"""
def find02():
    list = []
    for item in list01:
        if item.sex == "男":
            list.append(item)
    return list

# stu=find02()
# for item in stu:
#     # print(item.print_info())
#     print(item.name,item.sex)

#####练习4
"""
# 练习3:定义函数,查找年龄>=30的学生数量
"""
def find03():
    i = 0
    for item in list01:
        if item.age >= 30:
            i += 1
    return i

# stu=find03()
# print(stu)

#####练习5
"""
# 练习4:定义函数,将list01中所有学生的成绩归零.
"""
def find04():
    list = []
    for item in list01:
        item.score = 0
        list.append(item)  ####自定义存的类的对象
    return list

# stu=find04()
# for item in stu:
#     print(item.score)
#     print(item.print_info1())######有返回值
#     print(item.print_info2())######没有返回值，默认为ｎｏｎｅ

#####练习６
"""
# 练习5:获取list01中所有学生的名字
"""
def find05():
    list = []
    for item in list01:
        list.append(item.name)  ####注意ｌｉｓｔ中添加的是ｌｉｓｔ０１列表中的全部参数还是一个参数
    return list
    # print(list)

# stu=find05()
# print(stu)

#####练习７
"""
# 练习6:定义函数，在list01中查找年龄最大的学生对象
"""
####下述代码求出的是年龄最大的数，并不能打印出这个人的信息
def find06():
    max_age = 0
    for item in list01:
        if item.age > max_age:
            max_age = item.age
    return max_age

####下述代码能打印出年龄最大的人的信息
def find07():
    max_age = list01[0]
    for item in range(len(list01)):
        if list01[item].age > max_age.age:
            max_age = list01[item]
    return max_age

# stu=find07()
# print(stu.print_info1())

#####练习8
"""
    练习：定义对象计数器。
    定义老婆类，创建３个老婆对象。
    可以通过类变量记录老婆对象个数，
    可以通过类方法打印老婆对象个数。
    要求：画出内存图.
"""
class Person():
    wife_total = 3

    def __init__(self, wife, name, sex):
        ###实例数据
        self.name = name
        self.sex = sex
        Person.wife_total -= wife
# wife01=Person(1,"asd","nv")
# wife02=Person(1,"sd","nv")
# print("老婆还有%d个"%Person.wife_total)

class Wife():
    count = 0

    @classmethod
    ####定义类方法
    def print_count(cls):
        print("老婆有%d个" % cls.count)

    def __init__(self, name, sex):
        ###实例数据
        self.name = name
        self.sex = sex
        Wife.count += 1

wife01 = Wife("asd","nv")
wife02 = Wife("sd","nv")
wife03 = Wife("asd","nv")
wife04 = Wife("sd","nv")
####通过实例变量打印
# print(Wife.count)
####通过类方法打印
# Wife.print_count()


