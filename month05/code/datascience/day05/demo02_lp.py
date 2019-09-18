# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
demo2_poly.py  预测
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
mp.plot(dates, closing_prices,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='AAPL CP')
# 线性预测
N = 3
# 预测每一天的股票价格
pred_price = np.zeros(closing_prices.size - 2 * N + 1)
for i in range(pred_price.size):
    A = np.zeros((N, N))
    for j in range(N):
        A[j,] = closing_prices[i + j:i + j + N]
    B = closing_prices[i + N:i + N * 2]
    x = np.linalg.lstsq(A, B)[0]
    # print(x)
    pred = B.dot(x)
    pred_price[i] = pred
    # print(pred,closing_prices[6])
print(pred_price)
mp.plot(dates[2 * N:], pred_price[:-1], 'o-', color='orangered', label='Prediction')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
