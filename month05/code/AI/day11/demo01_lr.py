"""
demo01_lr.py 线性回归
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 计算损失函数#xs,ys是矢量
xs = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
ys = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

# 梯度下降求得回归线
times = 1000
lrate = 0.01  # 学习率
w0, w1 = [1], [1]  # 初始化
epoches, losses = [], []
for i in range(1, times + 1):
    # 计算当前w0与w1下 损失函数值
    loss = ((w0[-1] + w1[-1] * xs - ys) ** 2).sum() / 2
    print('{:4}>w0={:.6f},w1={:.6f},loss={:.6f}'.format(i, w0[-1], w1[-1], loss))
    epoches.append(i)
    losses.append(loss)
    # 求w0方向上的偏导数
    d0 = (w0[-1] + w1[-1] * xs - ys).sum()
    # 求w1方向上的偏导数
    d1 = (xs * (w0[-1] + w1[-1] * xs - ys)).sum()
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)
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

# 绘制w0,w1，loss的变化曲线
mp.figure('Train Process', facecolor='lightgray')
mp.title('Train Process', fontsize=16)
# w0
mp.subplot(311)
mp.ylabel('w0', fontsize=14)
mp.grid(linestyle=':')
mp.plot(epoches, w0[:-1], color='red', label='w0')
mp.legend()
mp.tight_layout()
# w1
mp.subplot(312)
mp.ylabel('w1', fontsize=14)
mp.grid(linestyle=':')
mp.plot(epoches, w1[:-1], color='red', label='w1')
mp.legend()
mp.tight_layout()
# loss
mp.subplot(313)
mp.ylabel('loss', fontsize=14)
mp.grid(linestyle=':')
mp.plot(epoches, losses, color='red', label='loss')
mp.legend()
mp.tight_layout()

# 基于三维曲线绘制梯度下降的过程中的每个散点
n = 500
w0_grid, w1_grid = np.meshgrid(np.linspace(0, 9, n),
                               np.linspace(0, 3.5, n))
loss = np.zeros_like(w0_grid)
for x, y in zip(xs, ys):
    loss += (w0_grid + w1_grid * x - y) ** 2 / 2
mp.figure('Loss Function', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0', fontsize=14)
ax3d.set_ylabel('w1', fontsize=14)
ax3d.set_zlabel('loss', fontsize=14)
ax3d.plot_surface(w0_grid, w1_grid, loss, cmap='jet')
ax3d.plot(w0[:-1], w1[:-1], losses, 'o-', color='orangered',zorder=3)
mp.tight_layout()

# 以等高线的方式绘制梯度下降的过程。
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('w0', fontsize=14)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(w0_grid, w1_grid, loss, 10, cmap='jet')
cntr = mp.contour(w0_grid, w1_grid, loss, 10,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()

mp.show()
