"""
demo03_ac.py 人工分类
"""
import numpy as np
import matplotlib.pyplot as mp

# x是8行两列
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# 绘制分类分界线，把区间分为500*500网络矩阵，为每个网络预测类别。并设置颜色
# l, r = x[:, 0].min(), x[:, 0].max()
l, r = x[:, 0].min()-1, x[:, 0].max()+1
# b, t = x[:, 1].min(), x[:, 1].max()
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
# meshgrid网格化，横坐标和列坐标拆分成500*500的网格矩阵
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
"""
numpy.where(condition[, x, y])  
该函数可以接受一个必选参数condition，注意该参数必须是array型的，只不过元素是true或者是false
x,y是可选参数：如果条件为真，则返回x,如果条件为false，则返回y，注意condition、x、y三者必须要能够“广播”到相同的形状
返回结果：返回的是数组array或者是元素为array的tuple元组，如果只有一个condition，则返回包含array的tuple，如果是有三个参数，则
where的作用就是返回一个数组中满足条件的元素（True）的索引，且返回值是一个tuple类型，tuple的每一个元素均为一个array类型，array的值即对应某一纬度上的索引。

numpy.piecewise(x, condlist, funclist, *args, **kw)
参数一 x:表示要进行操作的对象
参数二：condlist，表示要满足的条件列表，可以是多个条件构成的列表
参数三：funclist，执行的操作列表，参数二与参数三是对应的，当参数二为true的时候，则执行相对应的操作函数。
返回值：返回一个array对象，和原始操作对象x具有完全相同的维度和形状
"""

# 针对每个grid_x与grid_y预测所属类别
grid_z = np.piecewise(grid_x, [grid_x > grid_y, grid_x < grid_y], [0, 1])
print(grid_z)
mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80, label='Simple')
mp.show()
