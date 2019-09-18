# -*- coding: utf-8 -*-

"""
demo07_profit.py  研究股票收益率
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
mp.figure('profit', facecolor='lightgray')
mp.title('profit', fontsize=16)
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

# 获取两只股票的收益率
bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

mp.plot(dates, bhp_returns, color='blue', linestyle='--', label='bhp_returns', alpha=0.1)
mp.plot(dates, vale_returns, color='red', linestyle='--', label='vale_returns', alpha=0.1)

# 卷积降噪
convolve_core = np.hanning(8)  # 生成对称的小于０　的随机数
convolve_core /= convolve_core.sum()  # 令卷积核的和为１
bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')

# 绘制卷积降噪线
mp.plot(dates[7:], bhp_returns_convolved, color='dodgerblue', label='bhp_returns_convolved', alpha=0.3)
mp.plot(dates[7:], vale_returns_convolved, color='orangered', label='vale_returns_convolved', alpha=0.3)

# 拟合这两条曲线，获取两组多项式系数
days = dates.astype('M8[D]').astype('i4')
bhp_p = np.polyfit(days[7:], bhp_returns_convolved, 3)
bhp_polyfit_y = np.polyval(bhp_p, days[7:])
vale_p = np.polyfit(days[7:], vale_returns_convolved, 3)  # 系数
vale_polyfit_y = np.polyval(vale_p, days[7:])
# 绘制拟合线
mp.plot(dates[7:], bhp_polyfit_y, color='dodgerblue', label='bhp_returns_polyfit')
mp.plot(dates[7:], vale_polyfit_y, color='orangered', label='vale_returns_polyfit')

# 求取两个收益率降噪曲线的交点
diff_p = np.polysub(bhp_p, vale_p)
xs = np.roots(diff_p)
print(xs.astype('i4').astype('M8[D]'))

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
