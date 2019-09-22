## numpy
### 1. numpy的ravel() 和 flatten()函数
- 简介

首先声明两者所要实现的功能是一致的（将多维数组降位一维）。这点从两个单词的意也可以看出来，ravel(散开，解开)，
flatten（变平）。两者的区别在于返回拷贝（copy）还是返回视图（view），numpy.flatten()返回一份拷贝，对拷
贝所做的修改不会影响（reflects）原始矩阵，而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用
reference的意味），会影响（reflects）原始矩阵。

- eg:
```ipython
In [1]: import numpy as np

In [2]: x=np.array([[1,2],[3,4]])

# flattenh函数和ravel函数在降维时默认是行序优先
In [3]: x.ravel()
Out[3]: array([1, 2, 3, 4])

In [4]: x.flatten()
Out[4]: array([1, 2, 3, 4])

# 传入'F'参数表示列序优先
In [5]: x.ravel('F')
Out[5]: array([1, 3, 2, 4])

In [6]: x.flatten('F')
Out[6]: array([1, 3, 2, 4])

#reshape函数当参数只有一个-1时表示将数组降为一维
In [7]: x.reshape(-1)
Out[7]: array([1, 2, 3, 4])

In [8]: x.T.reshape(-1)
Out[8]: array([1, 3, 2, 4])
```
两者的区别：
```
In [13]: x.ravel()[1]=10

In [14]: x
Out[14]: 
array([[ 1, 10],
       [ 3,  4]])

# flatten函数返回的是拷贝。
In [15]: x.flatten()[1]=0

In [16]: x
Out[16]: 
array([[ 1, 10],
       [ 3,  4]])
```
### 2. np.column_stack()和np.hstack(）
- 简介

np.column_stack()中的axis类似于np.hstack(tuple)。

关于np.hstack中的理解：Stack arrays in sequence horizontally (column wise)
np.hstack((a,b))，如果a、b是list，则在列上叠加；如果a、b是矩阵array，则在行相同时扩展列，行不变。
- eg:
括号内是列表
```ipython

In [26]: x
Out[26]: array([ 1, 10,  3,  4])

In [27]: y
Out[27]: array([[10, 20, 30, 40]])

In [28]: y=np.array([10,20,30,40])

In [29]: x
Out[29]: array([ 1, 10,  3,  4])

In [30]: y
Out[30]: array([10, 20, 30, 40])

In [31]: np.hstack((x,y))
Out[31]: array([ 1, 10,  3,  4, 10, 20, 30, 40])

In [32]: np.column_stack((x,y))
Out[32]: 
array([[ 1, 10],
       [10, 20],
       [ 3, 30],
       [ 4, 40]])
```
括号内是矩阵
```
In [33]: y=np.array([[10],[20],[30],[40]])

In [34]: x=np.array([[1],[2],[3],[4]])

In [35]: np.hstack((x,y))
Out[35]: 
array([[ 1, 10],
       [ 2, 20],
       [ 3, 30],
       [ 4, 40]])

In [36]: np.column_stack((x,y))
Out[36]: 
array([[ 1, 10],
       [ 2, 20],
       [ 3, 30],
       [ 4, 40]])

```