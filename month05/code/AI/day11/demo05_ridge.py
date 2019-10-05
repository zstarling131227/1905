"""
demo05_ridge.py 岭回归
"""
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import numpy as np

# 采集数据
x, y = np.loadtxt('../ml_data/abnormal.txt', delimiter=',', usecols=(0, 1), unpack=True)
print(x, y)
# 选择并创建模型
model = lm.LinearRegression()
x = x.reshape(-1, 1)  # 把x改为n行一列的二维数组
model.fit(x, y)
# 得到预测结果
pred_y = model.predict(x)

# 岭回归
model = lm.Ridge(150, fit_intercept=True, max_iter=1000)
model.fit(x, y)
ridge_pred_y = model.predict(x)

# 　画图
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, marker='o', s=70, label='Samples', color='blue')
mp.plot(x, pred_y, color='red', label='Linear Regression', linewidth=2)
mp.plot(x, ridge_pred_y, color='blue', label='Linear Regression', linewidth=2)
mp.legend()
mp.show()
