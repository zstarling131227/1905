# -*- coding: utf-8 -*-
"""
demo6_weekday.py  简单时间处理
统计每周一到周五的平均值
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


# 日月年转年月日的函数
def dmy2wday(dmy):  # 传过来的是第一列的值
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = time.date().weekday()
    return t


# 读文件
wdays, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes = np.loadtxt(
    '../da_data/aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7), unpack=True,
    dtype='f8, f8, f8, f8, f8,f8',
    converters={1: dmy2wday})
# print(wdays)

# 用于存储最终的结果
ave_price = np.zeros(5)
print(ave_price)
for wday in range(ave_price.size):
    ave_price[wday] = np.mean(closing_prices[wdays == wday])  # 掩码
print(ave_price)

# 数据的轴向汇总
ary = np.arange(1, 21).reshape(4, 5)
print(ary)


def func(array):
    return array.mean(),array.max()


# 汇总二维数组每一行的均值
r = np.apply_along_axis(func, 1, ary)
print(r)
# 汇总二维数组每一列的均值
r = np.apply_along_axis(func, 0, ary)
print(r)
