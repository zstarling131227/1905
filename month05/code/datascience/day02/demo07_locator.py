# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_locator.py  刻度定位器
"""
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.MultipleLocator(1)',
            'mp.NullLocator()',
            'mp.MaxNLocator(nbins=5)',
            'mp.FixedLocator(locs=[3, 6, 9])']

mp.figure('Locators', facecolor='lightgray')

for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    ax = mp.gca()
    # 只留下bottom 轴
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0.5))
    mp.xlim(1, 10)
    mp.yticks([])
    # 设置主刻度定位器
    ma_loc = eval(locator)
    ax.xaxis.set_major_locator(ma_loc)
    # 设置次刻度定位器
    mi_loc = mp.MultipleLocator(0.1)
    ax.xaxis.set_minor_locator(mi_loc)

mp.show()
