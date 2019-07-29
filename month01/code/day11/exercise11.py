"""
day11作业
1. 三合一
2. 当天练习独立完成(使用标准属性封装实例变量exercise03..)
3. 请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。
4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
"""

"""
3.请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    体会：对象区分数据的不同
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def teach(self, other, skill):
        print(self.name, "教", other.name, skill)

    def work(self, money):
        print(self.name, "上班挣了%d钱" % money)


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach(zm, "九阳神功")
zm.teach(zwj, "化妆")
zwj.work(10000)
zm.work(6000)

"""
4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
    体会：类区别行为的不同
"""


class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, other):
        # 打的逻辑
        print("玩家攻击敌人")
        # 通过敌人对象地址，调用实例方法.
        other.damage(self.atk)

    def damage(self, value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死喽")
        print("游戏结束")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        # 受伤的逻辑
        print("敌人受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法
    def __death(self):
        # 死亡的逻辑
        print("死亡")
        print("掉装备")
        print("加分")

    def attack(self, other):
        print("敌人攻击玩家")
        other.damage(self.atk)


p01 = Player(1000, 100)
e01 = Enemy(200, 10)
p01.attack(e01)
e01.attack(p01)

p01.attack(e01)