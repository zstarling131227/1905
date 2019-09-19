"""
demo09_lr.py 线性回归
"""
import numpy as np
import matplotlib.pyplot as mp

# 计算损失函数#xs，ys是矢量
xs = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
ys = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

# 梯度下降求得回归线
times = 1000
lrate = 0.01  # 学习率
w0, w1 = [1], [1]  # 初始化
for i in range(1, times + 1):
    # 求w0方向上的偏导数
    d0 = (w0[-1] + w1[-1] * xs - ys).sum()
    # 求w1方向上的偏导数
    d1 = (xs * (w0[-1] + w1[-1] * xs - ys)).sum()
    w0.append(w0[-1] - lrate * d0)
    w1.append(w0[-1] - lrate * d1)
print(w0[-1], w1[-1])

# （目标回归函数）通过最优的w0,w1，求得所有样本的预测输出y
pred_test_y = w0[-1] + w1[-1] * xs

# 绘制样本点
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.grid(linestyle=':')
mp.scatter(xs, ys, marker='D', s=70,
           label='Samples', color='blue')
mp.plot(xs, pred_test_y, color='red', label='Linear Regression', linewidth=2)
mp.legend()
mp.show()
