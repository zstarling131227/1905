# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_svmlinear.py  svm分类器
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.model_selection as ms
import sklearn.metrics as sm

# 读取数据
data = np.loadtxt('/home/tarena/zxl/1905/month05/code/AI/ml_data/multiple2.txt',
                  delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]
# 训练模型
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=7)
model = svm.SVC(kernel='linear')
model.fit(train_x, train_y)
# 针对测试集预测结果   评估分类效果
pred_test_y = model.predict(test_x)
# print(sm.refusion_matrix(test_y, pred_test_y))
print(sm.classification_report(test_y, pred_test_y))

# 绘制分类边界线
# 把区间分为500*500网格矩阵，为每个网格预测类别
# 并设置颜色
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(
    np.linspace(l, r, n), np.linspace(b, t, n))

# 针对每个grid_x与grid_y预测所属类别
mesh_x = np.column_stack(
    (grid_x.ravel(), grid_y.ravel()))
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)

# 绘制
mp.figure('SVM Classifier', facecolor='lightgray')
mp.title('SVM Classifier', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1],
           label='Samples', s=60, c=test_y,
           cmap='jet')
mp.show()