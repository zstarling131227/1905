"""
demo04_bin.py  二值化
二值化后的数组中每个元素非0即1
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 75, 5500],
])

print("公式", '*' * 50)
bin = sp.Binarizer(threshold=80)
result = bin.transform(raw_sample)
print(result)

print("掩码", '*' * 50)
raw_sample[raw_sample <= 80] = 0
raw_sample[raw_sample > 80] = 1
print(raw_sample)
