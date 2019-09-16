"""
demo04_svd.py 提取方阵图片的特征值与奇异值
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm

# 读取图片数据
# img = sm.imread('../da_data/lily.jpg')
img = sm.imread('../da_data/lily.jpg', True)  # True表示灰度处理
print(img)
print(img[0, 0])
print(img.shape)

# mp.figure('lily')
# # mp.imshow(img)
# mp.imshow(img, cmap='gray')
# mp.tight_layout()
# mp.show()


# 提取img矩阵的特征值与特征向量
img = np.mat(img)
eigvals, eigvecs = np.linalg.eig(img)
# 抹掉一部分特征值
# eigvals[250:] = 0
eigvals[100:] = 0
img2 = eigvecs * np.diag(eigvals) * eigvecs.I
# 只提取实部
img2 = img2.real

# 奇异值分解
U, sv, V = np.linalg.svd(img)
sv[50:] = 0
img3 = U * np.diag(sv) * V

mp.figure('Lily')
mp.subplot(221)
mp.imshow(img, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(222)
print(img3.dtype)
mp.imshow(img3, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(224)  # 121表示一行两列第二幅
print(img2.dtype)
mp.imshow(img2, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()
