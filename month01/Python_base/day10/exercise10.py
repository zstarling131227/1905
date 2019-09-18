"""
1.　三合一
2. 练习独立完成
3.
[
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
在二维列表中，获取13位置，向左，3个元素　
在二维列表中，获取22位置，向上，2个元素
在二维列表中，获取03位置，向下，2个元素
4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50

"""

"""
3.
[
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
在二维列表中，获取13位置，向左，3个元素
在二维列表中，获取22位置，向上，2个元素
在二维列表中，获取03位置，向下，2个元素
"""
class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
            在二维列表中获取指定位置，指定方向，指定数量的元素.
        :param target: 二维列表
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向
        :param count: 指定数量
        :return: 列表
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


# --------------测试代码-----------------
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# 在二维列表中，获取13位置，向左，3个元素
re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
for item in re:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
for item in re:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
for item in re:
    print(item)


"""
4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""
"""

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def print_self_info(self):
        print(self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]


#  查找姓名是"灭霸"的敌人对象
def find01():
    for item in list01:
        if item.name == "灭霸":
            return item


e01 = find01()
# 如果又找到，返回值为None
# 所以可以判断不是空，再调用其实例方法.
# if e01 != None:
if e01:
    e01.print_self_info()
else:
    print("没找到")


# 查找所有死亡的敌人
def find02():
    list_result = []
    for item in list01:
        if item.hp == 0:
            list_result.append(item)
    return list_result


re = find02()
for item in re:
    item.print_self_info()

#  计算所有敌人的平均攻击力
def calculate01():
    sum_atk =0
    for item in list01:
        sum_atk += item.atk
    return sum_atk / len(list01)

print(calculate01())

# 删除防御力小于10的敌人
def delete01():
    for i in range(len(list01)-1,-1,-1):
        if list01[i].defense <10:
            del list01[i]

delete01()
for item in list01:
    item.print_self_info()

# 将所有敌人攻击力增加50
def set01():
    for item in list01:
        item.atk += 50

set01()
for item in list01:
    item.print_self_info()
"""
