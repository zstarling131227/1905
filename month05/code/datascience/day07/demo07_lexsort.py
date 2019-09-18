"""
demo07_lexsort.py 联合间接排序
"""
import numpy as np

names = np.array(['huawei', 'apple', 'mi', 'oppo', 'vivo'])
prices = np.array([92, 83, 71, 92, 40, ])
volumes = np.array([100, 251, 4, 12, 709])

# 先按价格排序，再按销量排序
indices = np.lexsort((volumes, prices))
print(indices)
print(names[indices])  # 原码输出
# 按销量倒叙排序
indices = np.lexsort((-volumes, prices))
print(indices)
print(names[indices])

# 插序
indices = np.searchsorted(prices, volumes)  # 返回的是被插入的数组的插入位置
print(indices)
# print(prices)
# print(volumes)
d = np.insert(prices, indices, volumes)
print(d)
