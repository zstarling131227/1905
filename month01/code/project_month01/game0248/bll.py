"""
    2048 游戏逻辑控制器，负责处理游戏核心算法
    步骤：
1. 将之前完成的2048算法移动到
　　bll.py-->　GameCoreController　类中．
   变量：
       合并时使用的一维列表
       移动时使用的二维列表
   方法：
      零元素移至末尾()
      合并()
      上移动()
      下移动()
      .....
    温馨提示：注意命名(私有化)
"""
import random

from model import *


class GameCoreController:
    def __init__(self):  ###实例变量
        self.__list_merge = None
        self.__map = [
            [2, 2, 0, 0],
            [2, 2, 4, 4],
            [4, 0, 4, 2],
            [2, 2, 0, 0]
        ]

    @property  ###实例属性
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        for line in self.__map:  ###也可以用self.map，返回的是数据
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for i in self.__map:
            self.__list_merge = i[::-1]
            self.__merge()
            i[::-1] = self.__list_merge

    def __transpose_squre_matrix(self):
        for i in range(1, len(self.__map)):
            for j in range(i, len(self.__map)):
                self.__map[i - 1][j], self.__map[j][i - 1] = self.__map[j][i - 1], self.__map[i - 1][j]

    def __move_up(self):
        self.__transpose_squre_matrix()
        self.__move_left()
        self.__transpose_squre_matrix()

    def __move_down(self):
        self.__transpose_squre_matrix()
        self.__move_right()
        self.__transpose_squre_matrix()

    def move(self, direction):
        if direction == DirectionModel.UP:
            self.__move_up()
        elif direction == DirectionModel.DOWN:
            self.__move_down()
        elif direction == DirectionModel.LEFT:
            self.__move_left()
        elif direction == DirectionModel.RIGHT:
            self.__move_right()

    def random_num(self):
        if random.randint(1,10)==1:
            4
        else:
            2

#####-------------------代码测试
# if __name__ == "__main__":
#     controller = GameCoreController()
#
#     # controller.move_left()
#     # print(controller.map)
#
#     controller.move(DirectionModel.DOWN)
#     print(controller.map)
