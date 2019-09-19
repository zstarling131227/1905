# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo01_adaboost.py  正向激励
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm
import matplotlib.pyplot as mp

# 加载波士顿地区房价数据集
boston = sd.load_boston()
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)
names = boston.feature_names
# |CRIM|ZN|INDUS|CHAS|NOX|RM|AGE|DIS|RAD|TAX|PTRATIO|B|LSTAT|
# 犯罪率|住宅用地比例|商业用地比例|是否靠河|空质气量|房间数|年限|距中心区距离|路网密度|房产税|师生比|黑人比例|低地位人口比例|

# 打乱原始样本数据集
# random_state: 随机种子
# 随机种子相同时，shuffle随机打乱的结果也相同
x, y = su.shuffle(boston.data, boston.target,
                  random_state=7)
# 划分训练集与测试集   8:2
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 构建决策树模型 使用训练集训练
model = st.DecisionTreeRegressor(max_depth=4)
# 使用测试集测试，输出r2_score
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
dt_fi = model.feature_importances_

# 构建基于决策树的正向激励模型，训练并预测结果
import sklearn.ensemble as se
model = se.AdaBoostRegressor(
    model, n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
adaboost_fi = model.feature_importances_

# 绘制特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('DT Feature Importances', fontsize=14)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
xs = np.arange(len(dt_fi))
sorted_ind = dt_fi.argsort()[::-1]
mp.bar(xs, dt_fi[sorted_ind], color='dodgerblue',
       label='DT Feature Importances')
mp.xticks(xs, names[sorted_ind])
mp.legend()

mp.subplot(212)
mp.title('AdaBoost Feature Importances', fontsize=14)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
sorted_ind = adaboost_fi.argsort()[::-1]
mp.bar(xs, adaboost_fi[sorted_ind],
       color='orangered',
       label='AdaBoost Feature Importances')
mp.xticks(xs, names[sorted_ind])
mp.legend()

mp.tight_layout()
mp.show()