# -*- coding: utf-8 -*-

"""
demo06_polyfit.py
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    t = time.date().strftime('%Y-%m-%d')
    return t


dates, bhp_closing_prices = np.loadtxt(
    '../da_data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8',
    converters={1: dmy2ymd})
vale_closing_prices = np.loadtxt(
    '../da_data/vale.csv', delimiter=',',
    usecols=(6,))

# 绘制收盘价折线图
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
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

# 绘制两支股票的差价函数
diff_prices = bhp_closing_prices - vale_closing_prices
mp.plot(dates, diff_prices, color='dodgerblue', label='diff prices')

# 多项式拟合
days = dates.astype('M8[D]').astype('i4')
# P = np.polyfit(days, diff_prices, 3) # 3次方
P = np.polyfit(days, diff_prices, 4)  # 4次方
# 绘制多项式函数曲线
pred_y = np.polyval(P, days)
mp.plot(dates, pred_y, color='grey', label='Polyfit Line')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
