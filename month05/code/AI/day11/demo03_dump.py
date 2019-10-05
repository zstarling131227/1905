"""
demo03_dump.py  模型导出成文件
"""
import pickle

"""
demo02_LinearRegression.py 线性回归
"""
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import numpy as np

# 采集数据
x, y = np.loadtxt('../ml_data/single.txt', delimiter=',', usecols=(0, 1), unpack=True)
print(x, y)
# 选择并创建模型
model = lm.LinearRegression()
x = x.reshape(-1, 1)  # 把x改为n行一列的二维数组
model.fit(x, y)
# 得到预测结果
pred_y = model.predict(x)

# 评估模型误差
import sklearn.metrics as sm

print(sm.mean_absolute_error(y, pred_y))
print(sm.mean_squared_error(y, pred_y))
print(sm.median_absolute_error(y, pred_y))
print(sm.r2_score(pred_y, y))

# 将训练好的模型保存到磁盘中（导出到文件）
with open('../ml_data/lr.pkl', 'wb') as f:
    pickle.dump(model, f)

print("导出成功")

