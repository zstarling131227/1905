"""
demo05_ohe.py 独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [1, 3, 2],
    [7, 5, 4],
    [1, 8, 6],
    [7, 3, 9]
])
print(raw_sample)
ohe = sp.OneHotEncoder(sparse=False, categories='auto')  # 输出为完整矩阵，0 和1都显示
# ohe = sp.OneHotEncoder(sparse=False, categories='auto', dtype=int)  # 输出为完整矩阵，0 和1都显示
# ohe = sp.OneHotEncoder(sparse=True)   #输出为稀疏矩阵，只打印显示为1的下标
re = ohe.fit_transform(raw_sample)
print(re)

# 元素对应的独热编码
encode_dict = ohe.fit(raw_sample)
print(encode_dict)
res = encode_dict.transform(raw_sample)
print(res)
