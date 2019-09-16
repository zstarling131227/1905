"""
demo08_interp.py 插值
"""
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 找一组散列点坐标
min_x = -50
max_x = 50
dix_x = np.linspace(min_x, max_x, 13)
dix_y = np.sinc(dix_x)
mp.scatter(dix_x, dix_y, marker='D', s=60)

# 使用插值，使散列点连续化
linear = si.interp1d(dix_x, dix_y, kind='linear')
x = np.linspace(min_x, max_x, 1000)
y = linear(x)
mp.plot(x, y, label='linear', alpha=0.3, color='red')
# 三次样条插值，使散列点连续化
cubic = si.interp1d(dix_x, dix_y, kind='cubic')
x = np.linspace(min_x, max_x, 1000)
y = cubic(x)
mp.plot(x, y, label='cubic', alpha=0.3)

mp.show()
