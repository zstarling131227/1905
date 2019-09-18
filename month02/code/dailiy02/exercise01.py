'''
##########ｉｓ和　＝＝比较
x = "123"
y = "123"
q = [1, 2, 3]
p = [1, 2, 3]
z = set('1231')
w = set('1231')
a = (1, 2, 3)
b = (1, 2, 3)
s = {1: 4}
v = {1: 4}

print(id(x))
print(id(y))
print(id(p))
print(id(q))
print(id(z))
print(id(w))
print(id(a))
print(id(b))
print(id(s))
print(id(v))
print("=======")
print(x)
print(y)
print(p)
print(q)
print(z)
print(w)
print(a)
print(b)
print(s)
print(v)
print(x is y)
print(p is q)
print(z is w)
print(a is b)
print(s is v)
print("=========")
print(x == y)
print(p == q)
print(z == w)
print(a == b)
print(s == v)
print("=========")
print(q == b)
'''

'''
# b=[(1, 1, 36), (1, 2, 18), (1, 3, 12),(2, 2, 12),(2,5,4)]
# a=[]
# for i in b:
#     a.append(sum(i))
# print(a)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(a[i])
# print(a in b)
# print(sorted(a))
'''

'''
# a=[1, 6, 6]
# b=[2, 2, 9]
# print(a.count(max(a)))
# print(b.count(max(b)))
# b.remove(max(b))
# print(b)
'''

'''
##复制
import copy
kvps={'1':1,'2':2,'3':3}
kvps=['1',1,'2',2,'3',3]
kvps=['1',1,'2',[2,'3',3]]
thecopy=kvps
thecopy0=kvps.copy()
thecopy1=copy.copy(kvps)
thecopy2=copy.deepcopy(kvps)
print(id(kvps))
print(id(thecopy))
print(id(thecopy0))
print(id(thecopy1))
print(id(thecopy2))
print("========================")
print(kvps)
print(thecopy)
print(thecopy0)
print(thecopy1)
print(thecopy2)
print("========================")
kvps['1']=5
kvps[1]=5
kvps[3][0]=9
print(kvps)
print(thecopy)
print(thecopy0)
print(thecopy1)
print(thecopy2)
sum=kvps['1']+thecopy['1']
sum1=kvps['1']+thecopy1['1']
print(sum)
print(sum1)
'''

'''
########## if __name__ == '__main__'
print('hello world!')
print('__name__value:',__name__)
def  main():
    print("this message is from main function")
if __name__ == '__main__':
    main()
import print_func
print("done!")
'''

'''
a="a"
b="b"
c="c"
print(a>b)
print(a or c)
print(a<b or c)
print(False or c)
print(c or False)
print(a>b or False)
print("-------------")
print(False and c )
print(a>b and c )
print(True and c )
print(a<b and c )
print("-------------")
print(not a>"b")
print(not a<"b")
print(not a>b and c )
print(not (a>b and c ))
'''

'''
print('a','b',sep='kbdfgfg')
def getPairs(dict):
    for k,v in dict.items() :
        print(k,v,sep=':')
getPairs({ x : x ** 3 for x in (1,2,3,4)})
'''

'''
import time
print(time.ctime())
import time as ad
print(ad.ctime())
from time import ctime
print(ctime())
from time import *
print(ctime())
'''

'''
from sys import argv,path
for i in argv:
    print(i)
print(argv)
print('================python from import===================================')
print('path:', path)
'''

'''
a = 111
print(isinstance(a, int))
class A:
    pass
class B(A):
    pass
b=B()
class C(object):
    pass
c=C()
print(isinstance(A(), A))
print(isinstance(B(), A))
print(isinstance(b, A))
print(isinstance(b, B))
print("----------------")
print(type(A()) == A)
print(type(B()) == A)
print("----------------")
print(issubclass(A,A))
print(issubclass(A,B))
print(issubclass(B,A))
# print(issubclass(b,A))
print("----------------")
print(isinstance(c, C))
print(isinstance(C, object))
print(isinstance(c, object))
print(type(C()) == object)
print(issubclass(C,object))
# print(issubclass(c,object))
'''

'''
str1=''
list1=[]
list2=list()
tuple1=()
tuple2=tuple()
set1={}##不可以创建空集合
set2=set()
dict1={}
dict2=dict()
print("-----------------------------------------")
str2="sd"
list3 = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
list4 = list("'abcd', 786 , 2.23, 'runoob', 70.2 ")
tuple3 = ( 'abcd', 786 , 2.23, 'runoob', 70.2)
tuple4 = tuple( "'abcd', 786 , 2.23, 'runoob', 70.2")
set3={'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
set4=set("'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'")
dict3={'Runoob':1, 'Google':2, 'Taobao':3}
dict4=dict(Runoob=1, Google=2, Taobao=3)
dict5=dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
tuple5 = (2,)
tuple6 = (2)
print(str1)
print(str2)
print(list1)
print(list2)
print(list3)
print(list4)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple6)
print(set1)
print(set2)
print(set3)
print(set4)
print(dict1)
print(dict2)
print(dict3)
print(dict4)
'''

'''
st="Mary,Jack"
st1=" ".join(st)
st2="".join(st)
print(st1)
print(st2)
print("-----------")
list="Mary, Jack"
l1=st.split(",")
l2=st.split(" ")
print(l1)
print(l2)
print("-----------")
list4 ="'abcd', 786 , 2.23, 'runoob', 70.2 "
print(list4.split(","))
print(list4.split(" "))
'''

'''
#####单前导下划线 _var
class Test:
   def __init__(self):
       self.foo = 11
       self._bar = 23
t=Test()
print(t.foo)
print(t._bar)
###实例化此类，并尝试访问在__init__构造函数中定义的foo和_bar属性,会看到_bar中的单个下划线
# 并没有阻止我们"进入"类并访问该变量的值
###This is print_module.py:
# def external_func():
#    return 23
# def _internal_func():
#    return 42

###前导下划线的确会影响从模块中导入名称的方式。如果使用通配符从模块中导入所有名称，
# 则Python不会导入带有前导下划线的名称（除非模块定义了覆盖此行为的__all__列表）
from print_module import *
print(external_func())
# print(_internal_func())
# # NameError: "name '_internal_func' is not defined"
###常规导入不受前导单个下划线命名约定的影响
import print_module
print(print_module.external_func())
print(print_module._internal_func())

#####单末尾下划线 var_
###一个变量的最合适的名称已经被一个关键字所占用
# def make_object(name,class):##SyntaxError: "invalid syntax"
#     pass
###一个变量的最合适的名称已经被一个关键字所占用,可以附加一个下划线来解决命名冲突
def make_object1(name,class_):
    pass

###双前导下划线 __var
class Test:
   def __init__(self):
       self.foo = 11
       self._bar = 23
       self.__baz = 23
t=Test()
print(dir(t))
###输出结果为：['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '_
# _module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
###self.foo变量在属性列表中显示为未修改为foo。self._bar的行为方式相同 - 它以_bar的形式显示在类上。
###会看到此对象上有一个名为_Test__baz的属性。 这就是Python解释器所做的名称修饰。 它这样做是为了防止变量在子类中被重写。
class ExtendedTest(Test):
   def __init__(self):
       super().__init__()
       self.foo = 'overridden'
       self._bar = 'overridden'
       self.__baz = 'overridden'
t2=ExtendedTest()
print(t2.foo)
print(t2._bar)
# print(t2.__baz)####AttributeError: "'ExtendedTest' object has no attribute '__baz'"
print(dir(t2))
###输出结果为：
# ['_ExtendedTest__baz', '_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '
# __weakref__', '_bar', 'foo']
###这个对象甚至没有__baz属性;可以看到__baz变成_ExtendedTest__baz以防止意外修改;但原来的_Test__baz还在
print(t2._ExtendedTest__baz)
print(t2._Test__baz)

###双下划线名称修饰对程序员是完全透明的
class ManglingTest:
   def __init__(self):
       self.__mangled = 'hello'
   def get_mangled(self):
       return self.__mangled
print(ManglingTest().get_mangled())
# ManglingTest().__mangled##AttributeError: "'ManglingTest' object has no attribute '__mangled'"

###名称修饰是否也适用于方法名称
class MangledMethod:
   def __method(self):
       return 42
   def call_it(self):
       return self.__method()
# MangledMethod().__method()##__methodAttributeError: "'MangledMethod' object has no attribute '__method'"
print(MangledMethod().call_it())

_MangledGlobal__mangled = 23
class MangledGlobal:
   def test(self):
       return __mangled
print(MangledGlobal().test())
###在这个例子中，我声明了一个名为_MangledGlobal__mangled的全局变量。然后我在名为MangledGlobal的类的上下文中访问变量。
# 由于名称修饰，我能够在类的test()方法内，以__mangled来引用_MangledGlobal__mangled全局变量。Python解释器自动将名称
# __mangled扩展为_MangledGlobal__mangled，因为它以两个下划线字符开头。这表明名称修饰不是专门与类属性关联的。
# 它适用于在类上下文中使用的两个下划线字符开头的任何名称。

###双前导和双末尾下划线 _var_
###Python保留了有双前导和双末尾下划线的名称，用于特殊用途。
#  这样的例子有，__init__对象构造函数，或__call__ --- 它使得一个对象可以被调用
class PrefixPostfixTest:
   def __init__(self):
       self.__bam__ = 42
print(PrefixPostfixTest().__bam__)

###单下划线 _
###单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color)
print(mileage)
print(_)
'''


# line2=urllib.quote(line.decode("gbk").encode('utf-16'))
# R1='gun\'s Not %s %%' %'UNIX'
# print(R1)
# a=range(100)
# print(a[2-3])
