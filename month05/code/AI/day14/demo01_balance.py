"""
demo01_balance.py 样本类别均衡化
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.model_selection as ms

# 加载数据
data = np.loadtxt('../ml_data/imbalance.txt', delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]
# 训练模型
train_x, test_x, train_y, test_y, = ms.train_test_split(x, y, test_size=0.25, random_state=7)
# 通过类别权重的均衡化，使所占比例较小的样本权重较高，而所占比例较大的样本权重较低，以此平均化不同类别样本对分类模型的贡献，提高模型性能。样本
# balanced是根据数量的比例来调整权重的
model = svm.SVC(kernel='linear', class_weight='balanced')
# {0: 20, 1: 1} 健表示类别，值表示权重
# model = svm.SVC(kernel='linear', class_weight={0: 20, 1: 1})
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
mp.figure('SVM Balance', facecolor='lightgray')
mp.title('SVM Balance', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
# 显示所有的样本
# mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=60, label='Simple')
# 显示测试的样本
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=60, label='Simple')
# print('test_y', test_y, sep='\n')
# print('predict_test_y', predict_test_y, sep='\n')
mp.show()
