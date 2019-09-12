"""
demo05_matrix.py 矩阵
"""

import numpy

# numpy.ndarray() # 两个数组相乘是数组对应元素相乘
# numpy.matrix()# 是矩阵的运算
# matrix是ndarray 的子类
ary = numpy.arange(1, 10).reshape(3, 3)
# m = numpy.matrix(ary, copy=False)  # 表示不独立，会更改
m = numpy.matrix(ary, copy=True)  # True 为默认值，是独立
print(m, type(m))
ary[0, 0] = 999
print(m, type(m))

# 测试数据拼块规则
m2 = numpy.mat(ary)
print(m2)

ary = '1,2,3;4,5,6;4,5,6'
m2 = numpy.mat(ary)
print(m2, type(m2))
