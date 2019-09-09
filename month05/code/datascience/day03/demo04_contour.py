# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
x:
0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3

y:
0 0 0 0
1 1 1 1 
2 2 2 2 
3 3 3 3

z:
2 2 2 2
2 4 4 2
2 4 4 2
2 2 2 2

demo04_contour.py   绘制等高线图
"""
import numpy as np
import matplotlib.pyplot as mp

# 整理数据
n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 网上抄的，不要纠结  计算出每个坐标点的高度
z = (1 - x / 2 + x**5 + y**3) * \
    np.exp(-x**2 - y**2)
# 绘制等高线
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=18)
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.5)
# 绘制等高线的高度标签文本
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)

# 填充等高线
mp.contourf(x, y, z, 8, cmap='jet')

mp.show()
