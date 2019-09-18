####练习１
"""
    定义父类
        动物（行为：叫）

    定义子类
        狗（行为：跑）
        鸟（行为：飞）

    创建三个类型的对象
    体会：isinstance(对象,类型)
    体会：issubclass(类型,类型)
"""
class Animal():
    def eat(self):
        print("会吃")


class Dog(Animal):
    def jump(self):
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飞")


# st01=Bird()
# st02=Dog()
# st03=Animal()
# print(isinstance(st01, Bird))###True
# print(isinstance(st01, Dog))###False
# print(isinstance(st02, Bird))###False
# print(issubclass(Animal, Dog))###False
# print(issubclass(Bird, Animal))###True
# print(issubclass(Animal, Bird))###False
# print(issubclass(Bird, Bird))###True

####练习2
"""
    定义父类
        车（数据：品牌,速度）

    定义子类
        电动车（数据：电池容量,充电功率）

    创建两个对象
    画出内存图.

"""
class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Moto(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


st01=Car("大众",78)
print(st01.brand)
st02=Moto("比亚迪",120,79,90)
print(st02.battery_capacity)
print(st02.brand)
####练习3
"""
(看内存图)

    手雷炸了，可能伤害敌人/玩家的生命.
             还可能伤害未知事物(鸭子.房子....)
    要求：增加了新事物，不影响手雷。
    体会：继承的作用
         多态的体现
         设计原则
            开闭原则
            单一职责
            依赖倒置
    画出设计图
    15:35
"""
class Granade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, damage_target):
        if not isinstance(damage_target, Damageable):
            raise ValueError("不是Damageable的子类")
        print("爆炸")
        damage_target.damage(self.atk)


class Damageable:
    def damage(self, value):
        # 如果子类
        raise NotImplementedError()

# -----------------------------------------
class Player(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("玩家死了")
        print("碎屏")


class Enemy(Damageable):
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("敌人受伤了")
        print("敌人")


g01 = Granade(100)
e01 = Enemy(100)
P01 = Player(100)
g01.explode(e01)
g01.explode(P01)
####练习4
"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置
"""
class GraphicManager:
    def __init__(self):
        self._graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self._graphics.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        for item in self._graphics:
            total_area += item.caculate_area()
        return total_area


class Graphic:
    def caculate_area(self):
        # pass
        raise NotImplementedError()


# -----------------------------------
class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def caculate_area(self):
        return 3.14 * self.radius ** 2


class rectangle(Graphic):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def caculate_area(self):
        return self.length * self.width


c01 = Circle(5)
r01 = rectangle(12, 4)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)
re = manager.get_total_area()
print(re)


####老师讲
"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__graphics:
            # 多态：
            # 调用的是图形
            # 执行的是圆形/矩形...
            total_area += item.calculate_area()
        return total_area

class Graphic:
    def calculate_area(self):
        # 如果子类不重写，则异常.
        raise NotImplementedError()
#-----------------------------------
class Circle(Graphic):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius **2


class Rectanlge(Graphic):
    def __init__(self,length,width):
        self.lenght = length
        self.width = width


    def calculate_area(self):
        return self.lenght *  self.width


# c01 = Circle(5)
# r01 = Rectanlge(10,20)
# manager = GraphicManager()
# manager.add_graphic(c01)
# manager.add_graphic(r01)
# re = manager.get_total_area()
# print(re)

