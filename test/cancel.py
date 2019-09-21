# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_gscv.py  GridSearchCV 网格搜索
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

# 网格搜索获取最优模型
model = svm.SVC(probability=True)
# 整理网格搜索所需要的超参数列表
params = [
    {'kernel': ['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel': ['poly'], 'C':[1],
     'degree': [2, 3]},
    {'kernel': ['rbf'], 'C':[1, 10, 100, 1000],
     'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(model, params, cv=5)
model.fit(train_x, train_y)
# 获取GridSearch的副产品
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
# 输出每组超参数的测试集得分
params = model.cv_results_['params']
scores = model.cv_results_['mean_test_score']
for p, s in zip(params, scores):
    print(p, '-->', s)


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

# 新增样本，得到每个样本的预测输出与置信概率
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
print(pred_prob_y)
# 置信概率矩阵
probs = model.predict_proba(prob_x)
print(probs)


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

# 绘制每个测试样本，并给出标注
mp.scatter(prob_x[:, 0], prob_x[:, 1],
           c=pred_prob_y,
           cmap='jet_r', s=80, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})

mp.show()