import numpy as np
import pandas as pd

unsorted_df = pd.DataFrame(np.random.randn(10, 2),  # 随机生成10行两列的数据
                           index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print('未排序', '-' * 59)
print(unsorted_df)
sorted_df = unsorted_df.sort_index()
print('按照行标（索引）进行升序排序', '-' * 59)
print(sorted_df)
print('按照字段名进行降序排序', '-' * 59)
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Minsu', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
unsorted_df = pd.DataFrame(d)
print('未排序', '-' * 59)
print(unsorted_df)
print('按照列名(年龄)进行降序排序', '-' * 59)
sorted_df = unsorted_df.sort_values(by='Age')  # 默认是升序
# sorted_df = unsorted_df.sort_values(by='Age', ascending=False)
print(sorted_df)
print('按照列名（先按年龄，再按评分）进行降序排序', '-' * 59)
# 对应的列按照对应的ascending顺序排序
sorted_df = unsorted_df.sort_values(by=['Age', 'Rating'], ascending=[False, True])
print(sorted_df)
