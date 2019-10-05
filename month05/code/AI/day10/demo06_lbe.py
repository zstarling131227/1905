"""
demo06_lbe.py 标签编码（连续值适用）
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford',
    'audi'])
print(raw_samples)
lbe = sp.LabelEncoder()
print(lbe)
# 默认按首字母排序
re = lbe.fit_transform(raw_samples)
print(re)
# 逆向编码
sample = lbe.inverse_transform(re)
print(sample)
