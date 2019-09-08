# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_plot.py  基本绘图
"""
import numpy as np
import matplotlib.pyplot as mp

# 绘制一条正弦曲线
x = np.linspace(-np.pi, np.pi, 1000)
print(x.shape)
# 矢量化的sin方法将会返回每个x对应的y
sinx = np.sin(x)
# 绘制一条余弦曲线   cos(x)/2
cosx = np.cos(x) / 2
# cosx = np.cos(x)

# 设置坐标轴的范围   第一象限
# mp.xlim(0, np.pi + 0.1)
# mp.ylim(0, 1.1)

# 修改坐标轴刻度
mp.xticks(
    [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    [r'$-\pi$', r'$-\frac{\pi}{2}$', '0',
     r'$\frac{\pi}{2}$', r'$\pi$'])
mp.yticks([-1.0, -0.5, 0, 0.5, 1])

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# 绘制特殊点
px = [3 / 4 * np.pi, 3 / 4 * np.pi]
py = [np.sin(px[0]), np.cos(px[1]) / 2]
mp.scatter(px, py, marker='o', color='red',
           s=70, label='Points', zorder=3)


# 添加备注
mp.annotate(
    r'$[\frac{3\pi}{4}, \frac{cos(\frac{3\pi}{4})}{2}]$',
    xycoords='data',
    xy=(3 / 4 * np.pi, np.cos(px[1]) / 2),
    textcoords='offset points',
    xytext=(-80, -30),
    fontsize=14,
    arrowprops=dict(
        arrowstyle='-|>',
        connectionstyle='angle3'
    )
)

mp.plot(x, sinx, linestyle='--', alpha=0.8,
        linewidth=2, color='dodgerblue',
        label=r'$y=sin(x)$')
mp.plot(x, cosx, linestyle='-.', alpha=0.8,
        linewidth=2, color='orangered',
        label=r'$y=\frac{1}{2}cos(x)$')


mp.legend()
mp.show()
