# -*- coding: utf-8 -*-

"""
demo04_cov.py  协方差
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
mp.plot(dates, bhp_closing_prices, alpha=0.9,
        color='dodgerblue', linewidth=2,
        linestyle='--', label='BHP')
mp.plot(dates, vale_closing_prices, alpha=0.9,
        color='orangered', linewidth=2,
        linestyle='--', label='VALE')

# 计算两支股票的协方差
ave_bhp = bhp_closing_prices.mean()
ave_vale = vale_closing_prices.mean()
dev_bhp = bhp_closing_prices - ave_bhp
dev_vale = vale_closing_prices - ave_vale
# cov = np.mean(dev_bhp * dev_vale)
cov = (dev_bhp * dev_vale).sum()/(dev_bhp.size-1)
print(cov)
# 相关系数
k = cov / (np.std(bhp_closing_prices) * np.std(vale_closing_prices))
print(k)
# 相关矩阵
print(np.corrcoef(bhp_closing_prices,vale_closing_prices))
print(np.cov(bhp_closing_prices,vale_closing_prices))


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
