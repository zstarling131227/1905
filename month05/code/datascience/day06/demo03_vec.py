"""
demo03_vec.py 函数矢量化
"""
import matplotlib.pyplot as mp
import numpy as np
import math as m


def foo(x, y):
    return m.sqrt(x ** 2 + y ** 2)  # 报错。math.sqrt只能处理标量.需要做矢量化处理
    # return np.sqrt(x ** 2 + y ** 2)  # 不报错

# 也可以这么写
# np.vectorize(foo)(a, b)

a, b = 3, 4
# a, b = np.arange(3, 6), np.arange(4, 7)
a, b = np.arange(3, 9).reshape(2, 3), np.arange(4, 10).reshape(2, 3)
print("a:", a)
print("b:", b)
# print(foo(a, b))
# 矢量化处理foo函数，使之可以处理矢量数据
foo_vec = np.vectorize(foo)  # 要求ａ,与ｂ 的维度相同
# print(foo_vec(a, b))
print(foo_vec(a, 6))  # 一个矢量一个标量也可以
