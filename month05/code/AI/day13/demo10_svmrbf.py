"""
demo10_rbf.py 支持向量机分类器（径向基核函数）
"""
# support vector machine SVM
import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.model_selection as ms

# 加载数据
data = np.loadtxt('../ml_data/multiple2.txt', delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]
# 训练模型
train_x, test_x, train_y, test_y, = ms.train_test_split(x, y, test_size=0.25, random_state=7)
# model = svm.SVC() # 默认是kernel='rbf',gamma=1
# 标准差为gamma，不能太大也不能太小，否则不容易切割。Ｃ是正则项。
model = svm.SVC(kernel='rbf', C=600, gamma=0.01)
model.fit(train_x, train_y)
# 针对测试集预测结果 评估分类效果
predict_test_y = model.predict(test_x)
print(sm.classification_report(test_y, predict_test_y))

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
mp.figure('SVM calssifier', facecolor='lightgray')
mp.title('SVM calssifier', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
# 显示所有的样本
# mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=60, label='Simple')
# 显示测试的样本
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=60, label='Simple')
mp.show()
