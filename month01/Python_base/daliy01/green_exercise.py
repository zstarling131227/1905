"""
class Test:
    def prt(self):###self 代表的是类的实例，代表当前对象的地址
        print(self)
        print(self.__class__)

t = Test()
t.prt()

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()

"""
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# day9补充：

# class Wife:
#     def __init__(ing,name,sex):
#         ing.xingming=name
#         ing.sex=sex
#     def play(self):
#         print(self.xingming+"王八蛋")
# w01=Wife("钥玥","女")
# w01.play()

####生成器（调试）
# import sys
#
# def fibonacci(n,w=0): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         print('%d,%d' % (a,b))
#         counter += 1
# f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print (next(f), end=" ")
#     except :
#         sys.exit()
#
# tuple01=(23,434,2,34)
# tuple01=(2,3,4)
# for i in tuple01:
#     print(i)

# ######随机数
# import numpy as np
# re=np.random.randint(1, 10)
# print(re)
# def random_index(rate):
#     start = 0
#     index = 0
#     randnum = np.random.randint(1, sum(rate))
#
#     for index, scope in enumerate(rate):
#         start += scope
#         if randnum <= start:
#             break
#     return index

# def main():
#     arr = ['red', 'green', 'blue']
#     rate = [45, 30, 25]
#     red_times = 0
#     green_times = 0
#     blue_times = 0
#     for i in range(10000):
#         if arr[random_index(rate)] == 'red':
#             red_times += 1
#         if arr[random_index(rate)] == 'green':
#             green_times += 1
#         if arr[random_index(rate)] == 'blue':
#             blue_times += 1
#
#     print(red_times, green_times, blue_times)
# if __name__ == '__main__':
#     main()


list01=[1,2,3,4,5]

for i in range(len(list01)-1,-1,-1):
    if list01[i]>3:
        list01.remove(list01[i])
print(list01)

for i in range(len(list01)-1,-1,-1):
    if list01[i] > 3:
        del list01[i]
print(list01)

for i in range(-len(list01),0):
    if list01[i]>3:
        del list01[i]
print(list01)

