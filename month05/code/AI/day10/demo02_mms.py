"""
demo02_mms.py 范围缩放（考虑列）
一般情况下会把特征值缩放至[0, 1]区间。
"""
import sklearn.preprocessing as sp
import numpy as np

# 列表中包含的每个列表表示一个样本，每个列表中的每一个元素表示每一个特征
raw_sample = np.array([
    [17, 100, 4000],
    [20, 80, 5000],
    [23, 75, 5500],
])
# print(raw_sample)
print("手动", '*' * 50)
mms_sample = raw_sample.copy()
# print(mms_sample.T)  # 求转置
for col in mms_sample.T:
    # print(col)
    col_min = np.min(col)
    col_max = np.max(col)
    a = np.array([
        [col_min, 1],
        [col_max, 1]
    ])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    # x = np.linalg.lstsq(a, b)
    print("斜率和截距",'-' * 30, x, sep='\n')
    # print(x[0], x[1])
    col = col * x[0]
    col = col + x[1]
    print(col)

print("公式", '*' * 50)
# 根据给定范围创建一个范围缩放器，feature_range表示缩放特征区间
mms = sp.MinMaxScaler(feature_range=(0, 1))
print(mms)
# 用范围缩放器实现特征值的范围缩放
mms_samples = mms.fit_transform(raw_sample)
print(mms_samples)
