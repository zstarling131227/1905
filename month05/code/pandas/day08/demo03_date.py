"""
demo03_datetimeindex.py 日期序列
"""
import pandas as pd

# 默认为天
dates = pd.date_range('2019-8-20', periods=5, freq='D')
print(dates)
dates = pd.date_range('2019-8-20', periods=5, freq='M')
print(dates)
dates = pd.date_range('2019-8-20', periods=5, freq='Y')
print(dates)
print('-' * 50)

# 构建
start = pd.datetime(2019, 8, 1)
end = pd.to_datetime('2019-8-10')
dates = pd.date_range(start, end)
print(dates)
print(pd.Series(dates).dt.day)
print('-' * 50)

# bdate_range
dates = pd.bdate_range('2019/08/01', periods=7)
print(dates)
