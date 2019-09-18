"""
demo_06.py 数组通用函数
"""
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
# 裁剪
b = np.ndarray.clip(a, min=3, max=7)
print(b)
print('-' * 50)

a = np.arange(100)
# print(a.compress((a % 3 == 0) and (a % 7 == 0)))# 报错
# 压缩，可以被掩码代替
r = a.compress(np.all([a % 3 == 0, a % 7 == 0], axis=0))
print(r)
b = np.ndarray.compress(a, a > 55)
print(b)
print('-' * 50)
