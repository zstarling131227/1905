import time
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print (time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

print (time.strftime("%U %c %d %H:%M:%S %Y", time.localtime()))

#####标记day15为根目录
# from my_project.common1.double_list_helper import *
# list01 = [
#     ["00", "01", "02", "03"],
#     ["10", "11", "12", "13"],
#     ["20", "21", "22", "23"],
# ]
# # 在二维列表中，获取13位置，向左，3个元素
# re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
# print(re)

# #####标记my_project为根目录
# from common1.double_list_helper import *
# list01 = [
#     ["00", "01", "02", "03"],
#     ["10", "11", "12", "13"],
#     ["20", "21", "22", "23"],
# ]
# # 在二维列表中，获取13位置，向左，3个元素
# re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
# print(re)

import sys
print(sys.path)
sys.path.append("/home/tarena/1905/month01/code/day15/my_project")
print(sys.path)

from main import *
# str01=time()
# str01.life_days(2019,6,21)
Time.life_days(2019,6,21)


