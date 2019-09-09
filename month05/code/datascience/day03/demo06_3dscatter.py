# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_3dsactter.py
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 300
# 标准正太分布
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
# 绘制3维散点图
mp.figure('3D Scatter', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=16)
ax3d.set_ylabel('y', fontsize=16)
ax3d.set_zlabel('z', fontsize=16)
d = x**2 + y**2 + z**2
ax3d.scatter(x, y, z, marker='o', s=70,
             c=d, alpha=0.5, cmap='jet')
# 紧凑布局
mp.tight_layout()
mp.show()
