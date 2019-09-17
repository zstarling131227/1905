"""
demo04_df.py DataFrame对象
"""
import numpy as np
import pandas as pd

data = [['Alex', 10], ['er', 12], ['re', 23]]
df = pd.DataFrame(data)
print(df)

# 指定column列名
df = pd.DataFrame(data, columns=['name', 'age'])
print(df)
print('-' * 50)
print(df.dtypes)  # 访问元素的数据类型

# 指定dtype：元素类型
df = pd.DataFrame(data, columns=['name', 'age'], dtype=float)
print(df)
print(df.dtypes)
print('-' * 50)

# 通过字典的方式创建DataFrame对象
# key为列名
data = {'name': ['tom', 'ty', 'yt'],
        'age': [23, 45, 23]}
df = pd.DataFrame(data)
print(df)

# 构建DataFrame对象的同时指定行标（index）
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df)
df = pd.DataFrame(data, index=pd.date_range('2019-8-10', periods=3))
print(df)
print('-' * 50)

# 其他情况   （每个字段一行记录）
data = [{'a': 1, 'b': 2},
        {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print('-' * 50)

# 从字典来创建DataFrame
data = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df)
print('-' * 50)

# 列查询（访问）
print(type(df['one']), df['one'])
print(df[['one', 'two']])
print('列查询（访问）', '-' * 50)
# 行查询（访问）
print(type(df[2:4]))
print(df[2:4])
# 通过行索引访问
print(df.loc['d'])
print(df.loc[['b', 'c']])
# 通过行索引下标访问行数据
print(df.iloc[2])
print(df.iloc[[2, 3]])
print('行查询（访问）', '-' * 50)

# 列添加
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
        'Age': [28, 34, 29, 42]}
# df = pd.DataFrame(data)  # 默认行标为01234……
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df)
# 行标相同才能添加，否则添加空值
# df['score']=pd.Series([90, 80, 70, 60])
df['score'] = pd.Series([90, 80, 70, 60], index=['a', 'b', 'c', 'd'])
print(df)
print('列添加', '-' * 50)

# 行添加
df = pd.DataFrame([['zs', 12], ['ls', 4]], columns=['Name', 'Age'])
print(df)
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], columns=['Name', 'Age'])
df = df.append(df2)
print(df)
# # 不可以添加series
# s = pd.Series(['tq', 7], index=['Name', 'Age'])
# df.append(s, ignore_index=False)
# print(df)
print('行添加', '-' * 50)

# 列删除
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print("dataframe is:")
print(df)
# #删除一列： one
del (df['one'])
print(df)
# #调用pop方法删除一列
df.pop('two')
print(df)
print('列删除', '-' * 50)

# 行删除
df = df.drop('d')
print(df)
print('行删除', '-' * 50)

# 更改数据
df = pd.DataFrame([['we', 334], ['rt', 56]], columns=['name', 'age'])
df2 = pd.DataFrame([['are', 34], ['tr', 506]], columns=['name', 'age'])
df = df.append(df2)
print(df)
df['name'][0] = 'tom'
print(df)
print('df.loc[1]:', df.loc[1], sep='\n')
df.loc[1]['age'] = 100
print(df)
print('更新数据', '-' * 50)

# 属性
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4'])
df['score'] = pd.Series([90, 80, 70, 60], index=['s1', 's2', 's3', 's4'])
print(df)
print(df.axes)
print(df['Age'].dtype)
print(df.empty)
print(df.ndim)
print(df.size)
print(df.values,type(df.values))
print(df.head(3))  # df的前三行
print(df.tail(3))  # df的后三行
