# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_pie.py  饼状图
"""
import numpy as np
import matplotlib.pyplot as mp

# 整理数据
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']

mp.figure('pie', facecolor='lightgray')
mp.axis('equal')
mp.pie(values, spaces, labels, colors, '%.2f%%',
       shadow=True, startangle=90, radius=1)
mp.show()
