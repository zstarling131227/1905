# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_figure.py
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Fi gure A', facecolor='gray')
mp.figure('Figure B', facecolor='lightgray')
mp.title('Figure B', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.tight_layout()
mp.show()
