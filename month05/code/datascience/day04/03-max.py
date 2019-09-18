# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
demo3_max.py  最值
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
lowest_prices, closing_prices, volume = np.loadtxt(
    '../da_data/aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7), unpack=True,
    dtype='M8[D], f8, f8, f8, f8,f8',
    converters={1: dmy2ymd})

# 30天股票的波动区间，最低价～最高价
max_price = highest_prices.max()
min_price = np.min(lowest_prices)
print('max:', max_price, 'min:', min_price)

# 最高点和最低点都是哪一天
max_ind = np.argmax(highest_prices)
min_ind = np.argmin(lowest_prices)
print('max date:', dates[max_ind])
print('min date:', dates[min_ind])

# maximum与minimum
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(a)
print(b)
print(np.maximum(a, b))
print(np.minimum(a, b))
