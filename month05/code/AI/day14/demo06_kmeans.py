"""
demo06_kmeans.py K均值聚类
"""
import sklearn.cluster as sc
import numpy as np
import matplotlib.pyplot as mp

# 加载数据
x = np.loadtxt('../ml_data/multiple3.txt', delimiter=',', dtype='f8')
# print(x)
print(x.shape)
# 做kmeans聚类分析  # n_clusters: 聚类数
model = sc.KMeans(n_clusters=4)
model.fit(x)
# 获取每个样本对应的类别标签
pred_label = model.labels_
print('pred_label:')
print(pred_label)
# 获取训练的聚类中心
centers = model.cluster_centers_
print('centers:')
print(centers)
print(centers[:, 0])
print(centers[:, 1])

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
mp.figure('Kmeans', facecolor='lightgray')
mp.title('Kmeans', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
# 显示所有的样本
mp.scatter(x[:, 0], x[:, 1], c=pred_label, cmap='jet', s=60, label='Kmeans')
# 显示聚类中心
mp.scatter(centers[:, 0], centers[:, 1], marker='+', color='red', s=300, label='centers')
mp.legend()
mp.show()
