# -*- coding: utf-8 -*-
"""
demo2_mean.py  算数平均数
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
mp.plot(dates, closing_prices, alpha=0.5,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='AAPL CP')

# 绘制30日收盘价均线
mean = np.mean(closing_prices, axis=0)  # 1是水平。0是垂直
# 也可以写成下述代码
# mean=closing_prices.mean()
mp.hlines(mean, dates[0], dates[-1], color='orangered', label='mean()')

# VWAP 交易量加权平均价格
VWAP = np.average(closing_prices, weights=volumes)
mp.hlines(VWAP, dates[0], dates[-1], colors='green', label='VWAP')

# TWAP 交易量加权平均价格
times = np.linspace(1, 7, 30)
TWAP = np.average(closing_prices, weights=times)
mp.hlines(TWAP, dates[0], dates[-1], color='blue', label='TWAP')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
