import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr, type(arr), arr.dtype)
# arr1 = arr.astype(float)
arr1 = arr.astype('float32')
print(arr1, type(arr1), arr1.dtype)
arr2 = arr.astype(str)
print(arr2, type(arr2), arr2.dtype)
arr2.shape = (3, 2)
print(arr2, arr2.size, type(arr2))

print(arr + arr)
print(arr * 10)

print('===================================')
a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1, a1.shape)
print(a1.size, len(a1))
a = np.arange(0, 10, 2)
print(a)
b = np.zeros(10, dtype='int32')
print(b)
c = np.ones(10, dtype='float32')
print(c)
d = np.zeros_like(a1)
print(d)
f = np.ones_like(a1)
print(f)
print('===================================')
a = np.arange(1, 9)
print(a)  # [1 2 3 4 5 6 7 8]

print('===================================')
b = a.reshape(2, 4)  # 视图变维  : 变为2行4列的二维数组
print(b)

print('=============视图变维======================')
b[0, 0] = 999
print(a, '\n', b)

print('===================================')
z = b.flatten()
print(z)
print('=============复制变维======================')
b[0, 0] = 888
print(b, '\n', z)

print('===================================')
c = b.reshape(2, 2, 2)  # 视图变维    变为2页2行2列的三维数组
print(c)
d = c.ravel()  # 视图变维	变为1维数组
print(d)
print('===============就地变维====================')
f = d.resize((2, 4))
print(d)
print(f)
