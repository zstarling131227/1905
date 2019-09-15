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
print('_'*50)

# 测试数据拼块规则
m2 = numpy.mat(ary)
print(m2)
print('_*50')

ary = '1,2,3;4,5,6;4,5,6'
m2 = numpy.mat(ary)
print(m2, type(m2))
print('_'*50)

# 测试矩阵的乘法运算法则
a = numpy.arange(1, 10).reshape(3, 3)
print(a)
print(a * a)  # 数组相乘
print(numpy.mat(a) * numpy.mat(a))  # 矩阵相乘
print('_'*50)

# 获取A矩阵的逆
a = numpy.mat('14 7 5;6 7 8; 4 4 10').reshape(3, 3)
print(a)
print(a.I)  # 任何矩阵都可以
print(a * a.I)
print(numpy.linalg.inv(a))  # 矩阵必须是方阵
print('_'*50)

# 应用题 解方程组
prices = numpy.mat('3 3.2; 3.5 3.6')
totals = numpy.mat('118.4; 135.2')
# x=numpy.linalg.lstsq(prices,totals)[0] # 求误差最小的一组结果
x = numpy.linalg.solve(prices, totals)  # 求唯一解
print(x)
persons = prices.I * totals
print(persons)
print(prices**0)
