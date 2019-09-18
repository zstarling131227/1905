"""
demo08_bitwise.py 位运算
"""
import numpy as np

# 位异或
a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
print(a, b)
c = a ^ b
print(c)
# c = a.__xor__(b)
# c = np.bitwise_xor(a, b)
# where方法返回c<0的元素的索引（就是下标）数组
print(np.where(c < 0))
print(np.where(c < 0)[0])

# 位与（判断是否是2的幂）
d = np.arange(1, 21)
print(d)
e = d & (d - 1)
# e = d.__and__(d - 1)
# e = np.bitwise_and(d, d - 1)
print(e)
print(e[e == 0])  # 掩码
print(d[e == 0])  # 掩码值
