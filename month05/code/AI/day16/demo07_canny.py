"""
demo07_canny.py 边缘识别
"""
import cv2 as cv

original = cv.imread('../ml_data/chair.jpg')
print(original.shape)
# cv.IMREAD_GRAYSCALE读图片的时候做灰度处理，把3维数组变成2维数组，只保留亮度通道
original = cv.imread('../ml_data/chair.jpg', cv.IMREAD_GRAYSCALE)
print(original.shape)
cv.imshow('Original', original)
# 索贝尔边缘识别
# cv.CV_64F：卷积运算使用数据类型为64位浮点型（保证微分的精度）
# 1：水平方向是否索贝尔偏微分
# 0：垂直方向是否索贝尔偏微分
# ksize：卷积核为5*5的方阵
hsobel = cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('H-Sobel', hsobel)
vsobel = cv.Sobel(original, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('V-Sobel', vsobel)
sobel = cv.Sobel(original, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('Sobel', sobel)
laplacian = cv.Laplacian(original, cv.CV_64F)
cv.imshow('Laplacian', laplacian)
# 　精度不大
# canny = cv.Canny(original, 150, 240)
canny = cv.Canny(original, 50, 240)
cv.imshow('Canny', canny)
cv.waitKey()
