"""
demo01_scale.py 均值移除（也就是标准化）（考虑列）
均值移除可以让样本矩阵中的每一列的平均值为0，标准差为1。
"""
import sklearn.preprocessing as sp
import numpy as np

raw_samples = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 75, 5500],
])
print("手动--------------------")
scale_sample=[]
for raw_sample in raw_samples.T:
    raw_mean = raw_sample.mean()
    # print(raw_mean)
    raw_diff = raw_sample - raw_mean
    # print(raw_diff)
    raw_std = np.std(raw_diff)
    # print(raw_std)
    raw_nstd = raw_diff / raw_std
    # print(raw_nstd)
    scale_sample.append(raw_nstd)
scale_sample=np.array(scale_sample).T
print(scale_sample)
print(scale_sample.mean(axis=0))
print(scale_sample.std(axis=0))

print("公式--------------------")
std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))  # axis=0表示垂直轴向，1表示水平轴向
print(std_samples.std(axis=0))
