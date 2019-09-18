"""
demo09_sin.py 三角函数 合成方波
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.zeros(1000)
n = 1000
# for i in range(1, n + 1):
#     y += 4 / ((2 * i - 1) * np.pi) * np.sin((2 * i - 1) * x)
for i in range(1, 4):
    y_ = 4 / ((2 * i - 1) * np.pi) * np.sin((2 * i - 1) * x)
    mp.plot(x, y_, alpha=0.5)
    y += y_

mp.plot(x, y, label='n=1000')
mp.legend()
mp.show()
