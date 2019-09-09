# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_imshow.py   热成像图
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
# 绘制热成像图
mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow', fontsize=18)
mp.grid(linestyle=':')
mp.imshow(z, cmap='jet', origin='lower')
mp.colorbar()
mp.show()
