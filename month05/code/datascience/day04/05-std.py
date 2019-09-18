# -*- coding: utf-8 -*-
"""
demo5_std.py  中位数
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


# 日月年转年月日的函数
def dmy2ymd(dmy):  # 传过来的是第一列的值
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = time.date().strftime('%Y-%m-%d')
    return t


# 读文件
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes = np.loadtxt(
    '../da_data/aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7), unpack=True,
    dtype='M8[D], f8, f8, f8, f8,f8',
    converters={1: dmy2ymd})


# 总体标准差
std = np.std(closing_prices)
print(std)
m = closing_prices.mean()
d = (closing_prices - m) ** 2
v = np.mean(d)
s = np.sqrt(v)
print(s)

# 样本标准差
std1 = np.std(closing_prices, ddof=1)
print(std1)
