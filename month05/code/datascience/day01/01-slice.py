import numpy as np

a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])  # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9
print('===================================')
a = np.arange(1, 28)
a.resize(3, 3, 3)
print(a)
print('===================================')
# 切出1页
print(a[1, :, :])
print('===================================')
# 切出所有页的1行
print(a[:, 1, :])
print('===================================')
# 切出0页的1行1列
print(a[0, :, 1])
print(a[0, 1, 1])
print(a[:2, :2, :1])

print('================掩码===================')
a = np.arange(10)
mask = [True, False, True, False, True, False, True, False, True, False]
print(a[mask])
a = np.array(['a', 'b', 'c', 'd'])
mask = [2, 3, 1, 1, 0, 0, 3, 2]
print(a[mask])
a = np.arange(1, 100)
print(a[(a % 3 == 0) & (a % 7 == 0)])

print('===================================')
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a, b))
print(c, c.shape)
# 垂直方向完成拆分操作，生成两个数组
d, e = np.vsplit(c, 2)
print(d, d.shape)
print(e, e.shape)

print('===================================')
# 水平方向完成组合操作，生成新数组
c = np.hstack((a, b))
print(c, c.shape)
# 水平方向完成拆分操作，生成两个数组
d, e, f = np.hsplit(c, 3)
print(d, d.shape)
print(e, e.shape)
print(f, f.shape)

print('===================================')
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
# 填充b数组使其长度与a相同
b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=-1)
print(b)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a, b))
print(c)

print('===================================')
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 深度方向（3维）完成组合操作，生成新数组
i = np.dstack((a, b))
print(i, i.shape)
# 深度方向（3维）完成拆分操作，生成两个数组
k, l = np.dsplit(i, 2)
print(k, '\n', l, l.shape)

print('===================================')
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.real, a.imag, sep='\n')
print(a.T)
print([elem for elem in a.flat])
b = a.tolist()
print(b)
print('===================================')
a = np.arange(1, 9)  # [1, 2, 3, 4, 5, 6, 7, 8]
b = np.arange(9, 17)  # [9,10,11,12,13,14,15,16]
# 把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
# 把两个数组组合在一起成两列
d = np.column_stack((a, b))
print(d)
print('===================================')

