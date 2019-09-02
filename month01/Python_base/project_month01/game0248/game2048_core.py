"""
    2048 游戏核心算法
"""
__list_merge = None

# 练习1.零元素移至末尾
# list_merge=[2,0,2,0]
#  [2,0,2,0]-->[2,2,0,0]
#  [2,0,0,2]-->[2,2,0,0]
#  [2,4,0,2]-->[2,4,2,0]
##########自己写，有问题
# for i in range(len(list_merge)+1):
#     for j in range(i+1):
#         if list_merge[i]<list_merge[i+1]:
#             list_merge[i],list_merge[i+1]=list_merge[i+1],list_merge[i]
def zero_to_end():
    """
    ０元素移至末尾
    :return:
    """
    # list_merge.append(1)##########局部变量可以直接改变全局变量所指向的对象，而不需要globa
    # 从后向前，如果发现０元素，删除并增加
    # -1 -2 -3 -4
    for i in range(-1, -len(__list_merge) - 1, -1):
        if __list_merge[i] == 0:
            del __list_merge[i]
            __list_merge.append(0)

# zero_to_end()
# print(list_merge)
# 练习２.零元素移至末尾
#  [2,2,0,0]-->[4,0,0,0]
#  [2,0,0,2]-->[4,0,0,0]
#  [2,0,4,2]-->[2,4,0,0]
#  [2,2,2,2]-->[4,4,0,0]
#  [2,2,2,0]-->[4,2,0,0]
def merge():
    """
    合并
    """
    ##现将中间的０元素移至末尾
    ##再合并相邻相同元素
    zero_to_end()
    ##########自己写，有问题
    # for i in range(0,len(list_merge)):
    #     for j in range(i,len(list_merge)):
    #         if list_merge[i]==list_merge[j]:
    #             list_merge[i]+=list_merge[i]
    #             list_merge[j]=0
    for i in range(len(__list_merge) - 1):
        ##将后一个累加到前一个之上
        if __list_merge[i] == __list_merge[i + 1]:
            __list_merge[i] += __list_merge[i + 1]
            del __list_merge[i + 1]
            __list_merge.append(0)

# merge()
# print(list_merge)
# 练习3.地图向左移动
map = [
    [2, 2, 0, 0],
    [2, 2, 4, 4],
    [4, 0, 4, 2],
    [2, 2, 0, 0]
]

# def move_left(list_target):
#     for i in range(len(list_target)):
#         list_merge=list_target[i]
#         merge()
def move_left():
    """
    向左移动
    :return:
    """
    # 思想：将二维列表中的每行（从左向右）交给ｍｅｒｇｅ函数进行操作
    for i in map:
        global __list_merge
        list_merge = i
        merge()

# move_left()
# print(map)

def move_right():
    """
   向右移动（看ｄａｙ１０　内存图）
   :return:
   """
    # 思想：将二维列表中的每行（从右向左）交给ｍｅｒｇｅ函数进行操作
    for i in map:
        global __list_merge
        #####从右向左取出数据形成新列表
        list_merge = i[::-1]###切片创建新的列表
        merge()
        #####从右向左接受合并后的数据
        i[::-1] = list_merge###切片是定位列表元素
# move_right()
# print(map)

# 练习４.地图向下移动(转置后为从右往左)，上移(转置后为从左往右)
map = [
    [2, 2, 0, 0],
    [2, 2, 4, 4],
    [4, 0, 4, 2],
    [2, 2, 0, 0]
]
def transpose_squre_matrix(squre_matrix):
    for i in range(1, len(squre_matrix)):
       for j in range(i, len(squre_matrix)):
           squre_matrix[i - 1][j], squre_matrix[j][i - 1]= squre_matrix[j][i - 1], squre_matrix[i - 1][j]
def move_up():
    transpose_squre_matrix(map)
    move_left()#上移
    # move_right()#下移
    transpose_squre_matrix(map)###转置的转置为原矩阵
def move_down():
    transpose_squre_matrix(map)
    move_right()#下移
    transpose_squre_matrix(map)###转置的转置为原矩阵

move_down()
print(map)