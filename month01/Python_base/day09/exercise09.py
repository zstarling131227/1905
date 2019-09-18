"""
day09 作业
1. 三合一(面向对象)
2. 复习购物车重构版本,体会重构作用.
3. 复习2048核心算法，体会降维思想.
4. (扩展)自行编写其他消除类游戏:消消乐,消灭星星...

"""


"""
5. 以万物皆对象的思想，洞察客观实物，
   随意创建两个类，四个对象，并调用其方法.
"""
class famliy():
    def __init__(self,name,relation):
        self.name=name
        self.relation=relation
    def travel(self,city):
        print(self.name+city)
father=famliy("爸爸","父女")
father.travel("稻城")
mother=famliy("妈妈","母女")
mother.travel("杭州")
sister=famliy("姐姐","姊妹")
sister.travel("北京")
brother=famliy("弟弟","姐弟")
brother.travel("南通")


class food():
    def __init__(self,food,taste,type):
        self.food_name=food
        self.taste=taste
        self.type=type
    def favorite(self,name):
        print(name+"最喜欢的的食物是："+self.type+self.taste + self.food_name)
favorite_food=food("红烧鱼","偏甜","蒸的")
favorite_food.favorite("爸爸")

class food():
    def __init__(self,food,taste="",type=""):
        self.food_name=food
        self.taste=taste
        self.type=type
    def favorite(self,name):
        print(name+"最喜欢的的食物是：",self.type,str(self.taste)+str(self.food_name))
favorite_food=food("红烧鱼","偏甜")
favorite_food.favorite("爸爸")
favorite_food=food("红烧鱼",type="偏甜")
favorite_food.favorite("爸爸")
favorite_food=food("红烧鱼","偏甜",type="蒸")
favorite_food.favorite("爸爸")
favorite_food=food("红烧鱼")
favorite_food.favorite("爸爸")


