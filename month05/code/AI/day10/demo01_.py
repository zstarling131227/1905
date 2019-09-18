"""
demo01_.py 均值移除（也就是标准化）
均值移除可以让样本矩阵中的每一列的平均值为0，标准差为1。
"""
import sklearn.preprocessing as sp
import numpy as np

raw_sample = np.array([
    [17, 100, 4000],
    [20, 85, 5000],
    [30, 75, 5500],
])
std_samples = sp.scale(raw_sample)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
