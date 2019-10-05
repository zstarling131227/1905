"""
demo04_sigmold.py  逻辑函数
"""

import numpy as np
import matplotlib.pyplot as mp


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.linspace(-50, 50, 1000)
y = sigmoid(x)
mp.plot(x, y)
mp.show()
