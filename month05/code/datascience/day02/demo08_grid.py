# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_grid.py  刻度网格线
"""
import numpy as np
import matplotlib.pyplot as mp

y = [1, 10, 100, 1000, 100, 10, 1]
mp.figure('Grid Line', facecolor='lightgray')
# 设置刻度定位器
ax = mp.gca()
x_ma_loc = mp.MultipleLocator(1)
ax.xaxis.set_major_locator(x_ma_loc)
x_mi_loc = mp.MultipleLocator(0.1)
ax.xaxis.set_minor_locator(x_mi_loc)

y_ma_loc = mp.MultipleLocator(250)
ax.yaxis.set_major_locator(y_ma_loc)
y_mi_loc = mp.MultipleLocator(50)
ax.yaxis.set_minor_locator(y_mi_loc)

# 设置刻度网格线
ax.grid(which='major', axis='both',
        linewidth=0.75, color='orangered',
        linestyle='-')
ax.grid(which='minor', axis='both',
        linewidth=0.25, color='orangered',
        linestyle='-')

mp.plot(y, 'o-', color='dodgerblue')
mp.show()
