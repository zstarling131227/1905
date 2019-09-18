import time

class Time:
    def life_days(year, month, day):
        """
            根据生日计算活了多少天
        :param year: 年
        :param month: 月
        :param day: 日
        :return: 活的天数
        """
        tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
        life_second = time.time() - time.mktime(tuple_time)
        return int(life_second / 60 / 60 // 24)

###分步调
# from  my_project.skill_system.skill_deployer import Car
# from  my_project.skill_system.skill_deployer import Moto
###整体调
# from my_project.skill_system1.skill_deployer import *
###以my_project为根目录
from skill_system1.skill_deployer import *

st01=Car("大众",78)
print(st01.brand)
st02=Moto("比亚迪",120,79,90)
print(st02.battery_capacity)
print(st02.brand)
