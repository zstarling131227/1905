"""
demo03_norm.py 归一化（也叫正则化）（考虑行）
归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。
变换后的样本矩阵，每个样本的特征值绝对值之和为1。
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 75, 5500],
])
print("手动", '*' * 50)
copy_raw = []
for row in raw_sample:
    row = row / np.abs(row).sum()
    # col /= np.abs(col).sum()  # 这种写法会直接改变raw_sample的值，但是在此处会报错
    # print(col)
    copy_raw.append(row)
print(np.array(copy_raw))
print(abs(np.array(copy_raw)).sum(axis=1))

print("公式", '*' * 50)
norm_sample = sp.normalize(raw_sample, norm='l1')   # l1是绝对值的和，l2表示的是平方和
print(norm_sample)
for i in range(len(norm_sample)):
    print(norm_sample[i].sum())
