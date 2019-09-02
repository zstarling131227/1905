#######练习１
"""
# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。
"""
####老师讲
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        # self.__hp = hp
        self.set_hp(hp)
        # self.__atk = atk
        self.set_atk(atk)

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")


e01 = Enemy("灭霸", 25, 120)
# e01.set_atk(20)
print(e01.get_atk())


#######练习２
"""
# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。
#    使用property封装变量
"""

####老师讲
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        # self.set_hp(hp)
        self.hp = hp
        # self.set_atk(atk)
        self.atk = atk

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")

    atk = property(get_atk, set_atk)

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")

    hp = property(get_hp, set_hp)


e01 = Enemy("灭霸", 100, 25)
e01.hp = 150
e01.atk = 30
print(e01.hp)
print(e01.__dict__)




#######练习３
"""
# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。
#    使用@property封装变量
"""

####老师讲


class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 10 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError("我不要")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")


e01 = Enemy("灭霸", 100, 25)
e01.hp = 150
e01.atk = 30
print(e01.hp)
print(e01.__dict__)


#######练习４
"""
    请以面向对象的思想，描述下列场景:
        小明在招商银行取钱
"""

####老师讲
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def draw_money(self, person, value):
        """
            取钱
        :param person:
        :param value:
        :return:
        """
        self.money -= value
        person.money += value
        print(person.name, "取了%d钱" % value)


xm = Person("小明", 0)
zsyh = Bank("招商", 100000)
zsyh.draw_money(xm, 10000)