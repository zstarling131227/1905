# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
demo4_profit.py  定义投资策略，拿历史数据进行验证
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
lowest_prices, closing_prices = np.loadtxt(
    '../da_data/aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6), unpack=True,
    dtype='M8[D], f8, f8, f8, f8',
    converters={1: dmy2ymd})

# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)  # 日月年转年月日的函数

mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置x轴刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
ax.xaxis.set_minor_locator(md.DayLocator())

# 为了日期显示合理，修改dates的dtype
dates = dates.astype(md.datetime.datetime)


def profit(opening_price, highest_price, lo_pr, clo_pr):
    # 定义买入卖出策略，通过开高低收计算当天收益
    # 如果低于开盘价0.01则买入，收盘价时卖出
    buying_pr = opening_price * 0.99
    if lo_pr <= buying_pr <= highest_price:
        return (clo_pr - buying_pr) / buying_pr
    return np.nan  # 当天没有交易


# 矢量化profit函数
profits = np.vectorize(profit)(opening_prices, highest_prices, lowest_prices, closing_prices)
print(profits)
nan_mask = np.isnan(profits)
print(nan_mask)
print(~nan_mask)  # ～表示按位取反，
# 绘制收益曲线
mp.plot(dates[~nan_mask], profits[~nan_mask], 'o-', color='dodgerblue', label='Profits')
print(profits[~nan_mask].mean())

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
