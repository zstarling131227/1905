'''
##self
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量

class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
'''

'''
class Test(object):
    def InstanceFun(self):
        print("InstanceFun")
        print(self)
    @classmethod
    def ClassFun(cls):
        print("ClassFun")
        print(cls)
    @staticmethod
    def StaticFun():
        print("StaticFun")

t = Test()
t.InstanceFun()# 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
Test.ClassFun()# 输出ClassFun，打印类位置 <class '__main__.Test'>
Test.StaticFun()# 输出StaticFun
t.StaticFun()# 输出StaticFun
t.ClassFun()# 输出ClassFun，打印类位置 <class '__main__.Test'>
# Test.InstanceFun() # 错误，TypeError: unbound method instanceFun() must be called with Test instance as first argument
# Test.InstanceFun(t)# 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
# t.ClassFun(Test) # 错误   classFun() takes exactly 1 argument (2 given)
'''

'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
print(myclass)
myiter = iter(myclass)
print(myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''

