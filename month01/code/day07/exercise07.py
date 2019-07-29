"""
day07 作业
1. 三合一
2. 当天练习独立完成
"""

"""
3. 定义在控制台中打印二维列表的函数
[
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]

1 2 3 44
4 5 5 5 65 6 87
7 5
"""
# def print_list():
#     """
#     打印原列表
#     :return:
#     """
#     list01=[
#         [1,2,3,44],
#         [4,5,5,5,65,6,87],
#         [7,5,9]
#     ]
#     print("[")
#     for j in list01:
#         print(j,end=",")
#         print()
#     print("]")
# print_list()

############固定参数
# def print_list1():
#     list01=[
#         [1,2,3,44],
#         [4,5,5,5,65,6,87],
#         [7,5,9]
#     ]
#     for i in range(len(list01)):
#         for j in range(len(list01[i])):
#             print(list01[i][j],end=" ")
#         print()
# print_list1()

############参数
def print_list2(list_target):
    """
    打印列表所有元素
    :param list_target: 目标列表
    :return:
    """
    for i in range(len(list_target)):
        for j in range(len(list_target[i])):
            print(list_target[i][j],end=" ")###########续行
        print()#####换行
# print_list2([[2,545,5,467,67],[77,7,7,6,7],[6,7,6,5,5,]])
list03=[[2,545,5,467,67],[77,7,7,6,7],[6,7,6,5,5,]]
print_list2(list03)

"""
4. (扩展)方阵转置.（不用做成函数）
    提示：详见图片.（看day07图片）(重点在推导过程)
"""
list01=[
    [1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]
# print(list01)
for i in list01:
    print(i ,end="\n")
######方法1
# for i in range(len(list01)):
#     for j in range(i):
#         list01[i][j],list01[j][i]=list01[j][i],list01[i][j]
###方法2
# for i in range(1,len(list01)):
#    for j in range(i,len(list01)):
#         list01[i-1][j],list01[j][i-1]=list01[j][i-1],list01[i-1][j]
for i in list01:
    print(i ,end="\n")

########老师讲

"""
4. (扩展)方阵转置.（不用做成函数）
    提示：详见图片.
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
"""
#list01[1][0] <->list01[0][1]
#list01[2][0] <->list01[0][2]
#list01[3][0] <->list01[0][3]

for r in range(1,4):
    #list01[r][0]<->list01[0][r]
    pass
#list01[2][1] <->list01[1][2]
#list01[3][1] <->list01[1][3]
for r in range(2,4):#2 3
    # list01[r][1] <->list01[1][r]
    pass
#list01[3][2] <->list01[2][3]
for r in range(3,4):
    # list01[r][2] <->list01[2][r]
    pass

for c in range(1,4):#1 2 3
    for r in range(c,4):
        list01[r][c-1],list01[c-1][r]=list01[c-1][r],list01[r][c-1]

"""

for c in range(1, len(list01)):  # 1 2 3
    for r in range(c, len(list01)):
        list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]

print(list01)









