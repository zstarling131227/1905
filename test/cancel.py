# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_quant.py  图像量化
"""
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import sklearn.cluster as sc
import matplotlib.pyplot as mp

img = sm.imread('/home/tarena/zxl/1905/month05/code/AI/ml_data/lily.jpg', True)
# 针对img 基于kmeans实现图像量化
x = img.reshape(-1, 1)
model = sc.KMeans(n_clusters=4)
model.fit(x)
labels = model.labels_  # 每个样本的类别标签
centers = model.cluster_centers_.ravel()
print(labels)
print(centers)
newimg = centers[labels].reshape(img.shape)

# 绘制
mp.figure('Quant', facecolor='lightgray')
mp.subplot(121)
mp.axis('off')  # 关闭坐标系
mp.imshow(img, cmap='gray')

mp.subplot(122)
mp.axis('off')  # 关闭坐标系
mp.imshow(newimg, cmap='gray')

mp.tight_layout()
mp.show()