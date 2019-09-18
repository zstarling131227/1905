"""
demo03_svd.py 提取奇异特征值
"""
import numpy as np

M = np.mat('4 11 14; 8 7 -2')
print(M)
# U, sv, V = np.linalg.svd(M)  # sv就是奇异值
# 奇异值适用于非方阵
U, sv, V = np.linalg.svd(M, full_matrices=False)  # 是否要求V是矩阵
print(U.shape, U * U.T)
print(V.shape, V * V.T)
print(sv)  # 奇异值
S = np.diag(sv)
print(S)
print(U * S * V)  # 报错
