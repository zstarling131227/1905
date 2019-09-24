"""
demo06_poly.py 多项式回归模型
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.metrics as sm

# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', delimiter=',', usecols=(0, 1), unpack=True)
print(x, y)

# 训练多项式回归模型
x = x.reshape(-1, 1)
# 10表示一元多项式的最高次
model = pl.make_pipeline(sp.PolynomialFeatures(10), lm.LinearRegression())
model.fit(x, y)
pred_y = model.predict(x)
# R2得分，(0,1]区间的分值。分数越高，误差越小。
print(sm.r2_score(y, pred_y))
# 绘制多项式曲线
px = np.linspace(x.min(), x.max(), 1000)
# px=np.linspace(x.min()-5,x.max()+5,1000)   # 区间值之外的数不能做预测
px_pred_y = model.predict(px.reshape(-1, 1))

# 　画图
mp.figure('Poly Regression', facecolor='lightgray')
mp.title('Poly Regression', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, marker='o', s=70, label='Samples', color='blue')
mp.plot(px, px_pred_y, color='red', label='Linear Regression', linewidth=2)
mp.legend()
mp.show()
