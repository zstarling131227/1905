# -*- coding: utf-8 -*-
"""
demo1_boll.py  布林线
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
mp.plot(dates, closing_prices, alpha=0.3,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='AAPL CP')

# 控制实体与影线的颜色(可以用掩码写)
rise = closing_prices >= opening_prices
color = np.array(['white' if x else 'green' for x in rise])
print(color)

ecolor = np.array(['red' if x else 'green' for x in rise])
# 绘制实体
mp.bar(dates, closing_prices - opening_prices, 0.8,
       opening_prices, color=color, edgecolor=ecolor, zorder=3, alpha=0.1)
# 绘制影线
mp.vlines(dates, lowest_prices, highest_prices, color=ecolor,alpha=0.1)

# 基于加权卷积实现5日移动均线
# 从y=e^x函数中找到递增的5个权重作为卷积核
x = np.linspace(-1, 0, 5)
kernel = np.exp(x)[::-1]
kernel /= kernel.sum()  # 让卷积核元素之和为1
print(kernel)
sma53 = np.convolve(closing_prices, kernel, 'valid')
mp.plot(dates[4:], sma53, color='green', label='SMA-53')

# 计算布林带的上轨和下轨
stds = np.zeros(sma53.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
upper = sma53 + 2 * stds
lower = sma53 - 2 * stds
mp.plot(dates[4:], upper, color='orangered', label='Upper')
mp.plot(dates[4:], lower, color='orangered', label='Lower')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
