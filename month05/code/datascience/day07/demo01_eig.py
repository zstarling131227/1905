"""
demo01_eig.py 特征值提取
"""
import numpy as np

# a = np.mat('3 4 7 6;4 5 2 2;6 5 6 7;7 8 4 2')
a = np.mat('1 6 3 7;3 8 4 6;1 4 9 5;6 8 3 5')
print(a)
# 提取特征值
print(np.diag(a))
eigvals, eigvecs = np.linalg.eig(a)
# 特征值
print('eigvals', eigvals, sep='\n')
# 特征向量
print('eigvecs', eigvecs, sep='\n')
print('+' * 50)
# 逆向推导原矩阵
eigvals[3:] = 0
print(eigvals)
a2 = eigvecs * np.diag(eigvals) * eigvecs.I
print(a2)
