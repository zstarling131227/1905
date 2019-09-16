"""
demo09_int.py 积分
"""

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc


def fun(x):
    return 2 * x ** 2 + 3 * x + 4


a, b = -5, 5
x = np.linspace(a, b, 1000)
y = fun(x)
mp.figure('line', facecolor='lightgray')
mp.title('line', fontsize=20)
mp.xlabel('x', fontsize=16)
mp.ylabel('y', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.plot(x, y, c='red', linewidth=6, label=r'$y=2x^2+3x+4$', zorder=0)

# 微积分法
n = 50
x2 = np.linspace(a, b, n + 1)
y2 = fun(x2)
area = 0
for i in range(n):
    # 上底加下底乘高除以2
    area += (y2[i] + y2[i + 1]) * (x2[i + 1] - x2[i]) / 2
print(area)
for i in range(n):
    # 四个点表示梯形的四个点。
    mp.gca().add_patch(mc.Polygon([
        [x2[i], 0], [x2[i], y2[i]],
        [x2[i + 1], y2[i + 1]], [x2[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))

import scipy.integrate as si

# 利用quad求积分 给出函数f，积分下限与积分上限[a, b]   返回(积分值，最大误差)
area = si.quad(fun, a, b)[0]
print(area)

mp.legend()
mp.show()
