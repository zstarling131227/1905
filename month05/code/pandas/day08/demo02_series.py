"""
demo02_series.py 测试ｐａｎｄａｓ的ｓｅｒｉｅｓ对象
"""
import numpy as np
import pandas as pd

data = np.array(['tom', 'pol', 'uiu'])
s = pd.Series(data)
print(s)
# index还可以是字符串
s = pd.Series(data, index=[10, 20, 30])
print(s)
# 访问series中的元素
print(s[10])
print('-' * 50)

# 从字典创建一个系列
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)
print(s + 1)
print(s['a'])
# 从标量创建一个系列
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

# 访问series中的元素
s = pd.Series([75, 76, 98, 97, 45], index=['a', 'b', 'c', 'd', 'e'])
# 访问下标为0 的元素，访问index为a的元素
print(s[0], s['a'])
print(s[:3])
print('-'*50)

# pandas识别的日期字符串格式
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01', '2011/05/01 01:01:01', '01 Jun 2011'])
print(dates)
dates=pd.to_datetime(dates)
print(dates)

# 日期运算
delta=dates-pd.to_datetime('1970-01-01')
print(delta,type(delta))


# 只有series才有dt接口
# 通过series的dt接口访问偏移量数据
print(delta.dt.days)
print(dates.dt.month)
