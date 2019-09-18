# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_gs.py  网格式布局  支持单元格合并
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid Layout', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, size=36, ha='center',
        va='center')
mp.xticks([])
mp.yticks([])

mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, 2, size=36, ha='center',
        va='center')
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 3, size=36, ha='center',
        va='center')
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, 4, size=36, ha='center',
        va='center')
mp.xticks([])
mp.yticks([])

mp.subplot(gs[2, 1:])
mp.text(0.5, 0.5, 5, size=36, ha='center',
        va='center')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
