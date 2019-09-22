"""
demo07_quant.py 图像量化
"""

import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
import sklearn.cluster as sc
import scipy.ndimage as sn

# 加载数据
img = sm.imread('../ml_data/lily.jpg',True)
print(img)
'''
img的输出结果为：
每一个元素代表的是每一个方格的灰度大小，centers表示的也是灰度大小
[[36.742 35.97  34.97  ... 54.102 54.33  51.042]
 [37.742 37.742 37.97  ... 54.102 53.33  51.042]
 [40.34  41.112 40.34  ... 51.732 51.846 50.857]
 ...
 [ 5.228  6.228  5.929 ... 71.666 68.954 68.242]
 [ 6.228  6.228  4.929 ... 73.182 72.182 71.242]
 [ 6.228  6.228  4.929 ... 69.709 71.709 74.242]]
'''
print(img.shape)

# 针对img,基于kmeans聚类分析做图像量化  # n_clusters: 聚类数
x = img.reshape(-1, 1)  # n行1列
print(x.shape)
model = sc.KMeans(n_clusters=4)
model.fit(x)
# 获取每个样本对应的类别标签
pred_label = model.labels_
print(np.unique(pred_label))
print('pred_label:')
print(pred_label)
# 获取训练的聚类中心
centers = model.cluster_centers_
print('centers:')
print(centers)
centers = model.cluster_centers_.ravel()
print('centers:')
print(centers)
# 掩码
new_img = centers[pred_label].reshape(img.shape)
print(new_img)
print(new_img.shape)

# 绘制
mp.figure('Quant', facecolor='lightgray')
mp.title('Quant img', fontsize=20)
mp.subplot(121)
mp.axis('off')
mp.imshow(img, cmap='gray')

mp.title('Quant new_img', fontsize=20)
mp.subplot(122)
mp.axis('off')
mp.imshow(new_img, cmap='gray')

mp.tight_layout()
mp.show()
