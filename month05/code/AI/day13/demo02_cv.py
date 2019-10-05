"""
demo02_cv.py 交叉验证
"""

import sklearn.model_selection as ms

import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb
import sklearn.model_selection as ms

# 加载数据
data = np.loadtxt('../ml_data/multiple1.txt', delimiter=',', dtype='f8')
print(data.shape)

# 整理数据集
x = data[:, :2]
y = data[:, 2]

# 训练集测试集划分(test_size=0.25测试数据数量)
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)

# 训练模型
model = nb.GaussianNB()

# 做5次交叉验证，若指标满意，再训练模型。cv表示交叉次数（就是指测试集的划分5次）scoring表示交叉验证指标
ac = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='accuracy')
print(ac)
ac = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='precision_weighted')
print(ac)
ac = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='recall_weighted')
print(ac)
ac = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='f1_weighted')
print(ac)
print(ac.mean())

model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)

# 　输出预测准确率
print((test_y == pred_test_y).sum() / test_y.size)

# 绘制分类分界线，把区间分为500*500网络矩阵，为每个网络预测类别。并设置颜色
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
# meshgrid网格化，横坐标和列坐标拆分成500*500的网格矩阵
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))

# 针对每个grid_x与grid_y预测所属类别
# 抻平矩阵，将500*500的矩阵转换成n行一列
mesh_x = np.column_stack((grid_x.ravel(), grid_y.ravel()))
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)
# 绘制
mp.figure('Naive Bayes', facecolor='lightgray')
mp.title('Naive Bayes', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=60, label='Simple')
mp.legend()
mp.show()
