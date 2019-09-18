"""
demo08_groupby.py 分组
"""
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                     'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
            'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
            'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)

grouped = df.groupby('Year')
print(grouped)  # 返回的是索引
print(grouped.groups)  # 返回的是原数据
for year, group in grouped:
    print(year)
    print(group)

print('产看2014 一个组的', '-' * 50)
print(grouped.get_group(2014))

print('聚合每一年的平均的分', '-' * 50)
print(grouped['Points'].agg(np.mean))
print('聚合每一年的分数之和，平均分', '标准差', '-' * 50)
print(grouped['Points'].agg([np.sum, np.mean, np.std]))
