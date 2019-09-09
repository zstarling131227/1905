# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_3dframe.py   3d线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 整理数据
n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 网上抄的，不要纠结  计算出每个坐标点的高度
z = (1 - x / 2 + x**5 + y**3) * \
    np.exp(-x**2 - y**2)

# 绘制
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
ax3d.plot_wireframe(
    # x, y, z, rstride=20, cstride=20,
    x, y, z, rstride=50, cstride=50,
    linewidth=1, color='dodgerblue')
mp.tight_layout()
mp.show()
