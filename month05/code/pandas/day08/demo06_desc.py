"""
demo06_desc.py  dateframe的描述性统计
"""
import numpy as np
import pandas as pd

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}

df = pd.DataFrame(d)
print(df)
print("-" * 50)
# 测试描述性统计函数
print(df.sum())  # 默认为垂直方向
print("-" * 50)
print(df.sum(1))  # 按水平方向相加
print("-" * 50)
print(df.mean())
print("-" * 50)
print(df.mean(1))
print("-" * 50)

# describe 描述性统计函数
print(df.describe())
print("-" * 50)
print(df.describe(include=['object']))
print("-" * 50)
