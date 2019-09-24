"""
demo04.py 分类报告
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb
import sklearn.model_selection as ms
import sklearn.metrics as sm

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

# 输出混淆矩阵
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)

# 输出分类报告
cr = sm.classification_report(test_y, pred_test_y)
print(cr)

mp.matshow(cm, cmap='gray')
mp.show()
