"""
demo10_star.py star特征点检测
"""
import cv2 as cv

original = cv.imread('../ml_data/table.jpg')
cv.imshow('Original', original)

gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# 创建star特征点检测器
star = cv.xfeatures2d.StarDetector_create()
# 检测出gray图像所有的特征点
keypoints = star.detect(gray)

mixture = original.copy()
# drawKeypoints方法可以把所有的特征点绘制在ｍｉｘｔｕｒｅ图像中　
# 圆圈的大小表示特征点的信息越强烈
cv.drawKeypoints(
    original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
