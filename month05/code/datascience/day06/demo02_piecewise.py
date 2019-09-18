import matplotlib.pyplot as mp
import numpy as np

a = np.array([-7, 8, 10, 0, -5])
re = np.sign(a)
print(re)
re = np.piecewise(a, [a < 0, a == 0, a > 0], [-1, 0, 1])
print(re)
