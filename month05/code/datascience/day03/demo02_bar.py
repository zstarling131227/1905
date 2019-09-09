# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_bar.py  柱状图
"""
import numpy as np
import matplotlib.pyplot as mp

apples = np.array([91, 86, 23, 89, 45, 62, 39, 84, 56, 23, 48, 95])
oranges = np.array([94, 59, 23, 21, 36, 91, 26, 23, 65, 23, 94, 56])

mp.figure('Bar Chart', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.xlabel('Month', fontsize=16)
mp.ylabel('Volume', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':', axis='y')
x = np.arange(12)
# 堆叠式
# mp.bar(x, apples, 0.8, color='dodgerblue',
#        label='Apple',align='edge')
# mp.bar(x, oranges, 0.8, color='orangered',
#        label='Orange',align='edge')
mp.bar(x - 0.2, apples, 0.4, color='dodgerblue',
       label='Apple',align='center')
mp.bar(x + 0.2, oranges, 0.4, color='orangered',
       label='Orange')
# 修改x的刻度文本
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr',
              'Mar', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
