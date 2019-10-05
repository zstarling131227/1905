"""
demo01_adaboost.py 正向激励
"""
import sklearn.ensemble as se
import sklearn.metrics as sm  # sklearn.metrics提供了计算模型误差的几个常用算法
import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su
import matplotlib.pyplot as mp
import numpy as np

# 加载波士顿地区房价数据集（字典类型）
boston = sd.load_boston()
# print(boston,sep="")
for i in boston:
    print(i)
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)
names = boston.feature_names
# |CRIM|ZN|INDUS|CHAS|NOX|RM|AGE|DIS|RAD|TAX|PTRATIO|B|LSTAT|
# 犯罪率|住宅用地比例|商业用地比例|是否靠河|空气质量|房间数|年限|距中心区距离|路网密度|房产税|师生比|黑人比例|低地位人口比例|

# 打乱原始数据集的输入和输出   random_state：随机种子，随机种子相同时，shuffle随机打乱的结果也相同
x, y = su.shuffle(boston.data, boston.target, random_state=7)
# print(x, y)
# 划分训练集和测试集 8:2
train_size = int(len(x) * 0.8)
train_x, text_x, train_y, text_y = x[:train_size], x[:train_size], y[:train_size], y[:train_size]

# 构建决策树模型 使用训练集训练
modle = st.DecisionTreeRegressor(max_depth=4)
# 使用测试集测试，输出r2_score
modle.fit(train_x, train_y)
pred_y = modle.predict(text_x)
re = sm.r2_score(text_y, pred_y)
print(re)
# 特征重要性
dt_fi = modle.feature_importances_
# print(dt_fi)

print('=' * 60)

# 创建基于决策树的正向激励回归器模型
# n_estimators：构建400棵不同权重的决策树，训练模型
model = se.AdaBoostRegressor(modle, n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_y = model.predict(text_x)
re = sm.r2_score(text_y, pred_y)
print(re)
# 特征重要性
ab_fi = model.feature_importances_
print(ab_fi)

# 绘制特征重要性
# 决策树回归器给出的特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('DT FI', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
xs = np.arange(len(dt_fi))
# sorted_index = dt_fi.argsort()  # 返回的是排序后的下标(默认是从低到高)
sorted_index = dt_fi.argsort()[::-1]  # 返回的是排序后的下标
mp.bar(xs, dt_fi[sorted_index], color='red', label='DT FI')
mp.xticks(xs, names[sorted_index])
mp.legend()

# # 基于决策树的正向激励回归器给出的特征重要性
mp.subplot(212)
mp.title('AB FI', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
sorted_index = ab_fi.argsort()[::-1]  # 返回的是排序后的下标
mp.bar(xs, ab_fi[sorted_index], color='red', label='AB FI')
mp.xticks(xs, names[sorted_index])
mp.legend()
mp.tight_layout()
mp.show()
