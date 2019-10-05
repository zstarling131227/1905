"""
demo09_box.py 角点检测
"""
import cv2 as cv

original = cv.imread('../ml_data/box.png')
cv.imshow('orginal', original)
gray = cv.cvtColor(original, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
# Harris角点检测器
# 边缘水平方向、垂直方向颜色值改变超过阈值7、5时即为边缘
# 边缘线方向改变超过阈值0.04弧度即为一个角点。
concers = cv.cornerHarris(gray, 7, 5, 0.04)
mixture = original.copy()
print(concers.max())
mixture[concers > concers.max() * 0.01] = [0, 0, 255]
cv.imshow('Corner', mixture)
cv.waitKey()
