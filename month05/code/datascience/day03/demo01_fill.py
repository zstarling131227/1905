# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo01_fill.py 填充图
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=18)
mp.grid(linestyle=':')
mp.plot(x, sinx, color='dodgerblue',
        label='sin(x)')
mp.plot(x, cosx, color='orangered',
        label='cos(x)')

# 绘制填充
mp.fill_between(x, sinx, cosx, sinx < cosx,
                color='dodgerblue', alpha=0.3)
mp.fill_between(x, sinx, cosx, sinx > cosx,
                color='orangered', alpha=0.3)


mp.legend()
mp.show()
