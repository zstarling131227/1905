# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo01_plot.py
"""
import numpy as np
import matplotlib.pyplot as mp

xs = np.arange(6)
ys = np.array([23, 62, 36, 42, 9, 12])
mp.plot(xs, ys)

# 绘制水平线与垂直线
mp.vlines([3, 5, 7, 8], 20, 50)
mp.hlines(30, 1, 4)

mp.show()
