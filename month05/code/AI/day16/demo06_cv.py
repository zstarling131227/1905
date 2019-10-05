"""
demo06_cv.py opencv  图像识别
"""
import numpy as np
import cv2 as cv

# 读取图片
img = cv.imread('../ml_data/forest.jpg')
# print(img)
'''
shape(3,3,3)
[
     [[x,x,x],[x,x,x],[x,x,x]],
     [[x,x,x],[x,x,x],[x,x,x]],
     [[x,x,x],[x,x,x],[x,x,x]]
]

img[:行, 列, 深度]
'''
"""img输出结果
[[[ 75 187 170]
  [ 81 187 180]
  [ 54 175 171]
  ...
  [ 29 176 184]
  [ 24 149 157]
  [  3 120 127]]
……
 [[ 29  40  38]
  [ 25  35  35]
  [ 20  33  35]
  ...
  [  9 100  91]
  [  9 105  94]
  [  9 107  95]]]
"""
print(img.shape, img[0, 0])
# 输出结果(397, 600, 3) [ 75 187 170]
# [ 75 187 170] 是bgr三种颜色（左上角顶角属于原点）
# (397, 600, 3)：三维数组（矩阵中每个元素包含3个数值）数组的size是397*600*3
# 以下两者类似
# (397, 600, 1)：三维数组（矩阵中每个元素包含1个数值）数组的size是397*600*1
# (397, 600)：二维数组（矩阵中每个元素就是一个数），数组的size是397*600

print(img.shape, img[0, 0, 0])
print(img.shape, img[0, 0, :2])
# 将矩阵img前6行6列所有深度的值设置为0
blue = np.zeros_like(img[:6, :6, :])  # 全为0的数组
print(blue)
print(blue.shape)
# 获取矩阵img前6行6列第一深度的值
test = img[:6, :6, 0]
print(test)
print(test.shape)
# 将矩阵img前6行6列第一深度的值赋值给矩阵blue
blue[:6, :6, 0] = test
print(blue)
print(blue.shape)

# 第一个'img'是标题，第二个是显示的图片
cv.imshow('img', img)

# 显示某个颜色通道的数据
# blue
# 将矩阵img设置为0并复制给变量blue
blue = np.zeros_like(img)  # 全为0的数组
# [:, :, 0]表示所有行的所有列下标为０的元素，bgr中就是值b(blue)，只保留蓝色部分
blue[:, :, 0] = img[:, :, 0]
cv.imshow('blue', blue)
# red
red = np.zeros_like(img)
red[:, :, 2] = img[:, :, 2]
cv.imshow('red', red)
# green
green = np.zeros_like(img)
green[:, :, 1] = img[:, :, 1]
cv.imshow('green', green)

# 图像裁剪
# (397, 600, 3)  397行，600列。故高度h=397,宽度w=600
h, w = img.shape[:2]  # 高度与宽度
l, t = int(w / 4), int(h / 4)  # 左、上
r, b = int(w * 3 / 4), int(h * 3 / 4)  # 右、下
# [t:b, l:r] 表示行和列，切取的是四个点连接围成的部分
img2 = img[t:b, l:r]
cv.imshow('croped', img2)

# 图像缩放     缩放到某个大小范围

# 图像缩小（就是删除行和列）
# (int(w / 4), int(h / 4))是宽和高都变成了原来的1/4，是等比例缩放，也可以不等比例缩放(int(w / 4), int(h))
img3 = cv.resize(img, (int(w / 4), int(h / 4)))
cv.imshow('img3', img3)

# 图像放大（就是对行和列做复制，做插值）
# 使x与y都放到原来的4倍
img4 = cv.resize(img3, None, fx=4, fy=4)
cv.imshow('img4', img4)

# 敲键盘任意值开始或结束
cv.waitKey()

# 保存图片
cv.imwrite('../ml_data/blue.jpg', blue)
