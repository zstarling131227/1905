"""
demo_add07.py 加法，乘法通用函数
"""
import numpy as np

a = np.arange(1, 10)
b = np.add(a, a)  # 两数组相加
c = np.add.reduce(a)  # a数组元素累加和
d = np.add.accumulate(a)  # 累加和过程
e = np.add.outer([10, 20, 30], a)  # 外和   [10,20,30]看做一个3*1矩阵，对a的每一个元素对应加上10 20 30
print('-' * 50)
f = np.outer([10, 20, 30], a)  # 外积   [10,20,30]看做一个3*1矩阵，对a的每一个元素对应乘上10 20 30
g = np.prod(a)  # 累乘
h = np.cumprod(a)  # 累乘积过程
print(a, b, c, d, e, f, g, h, sep='\n')
print('-' * 50)

# 测试除法通用符
a = np.array([20, 20, -20, -20])
b = np.array([3, 3, -6, 6])
print(np.true_divide(a, b))  # a 真除 b  （对应位置相除）
print(np.divide(a, b))  # a 真除 b
print(np.floor_divide(a, b))  # a 地板除 b	（真除的结果向下取整）
print(np.ceil(a / b))  # a 天花板除 b	（真除的结果向上取整）
print(np.trunc(a / b))  # a 截断除 b	（真除的结果直接干掉小数部分）
print(np.round(a / b))  # 四舍五入取整
print(np.floor(a / b))
