"""
demo08_equalhist.py 直方图均衡化亮度提升
"""
import cv2 as cv

original = cv.imread('../ml_data/sunrise.jpg')
cv.imshow('Original', original)

# 彩色图转换为灰色图（gray是二维数组）
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 对灰色图做处理
# 直方图（x表示样本，y表示样本数量）均衡化
equalized_gray = cv.equalizeHist(gray)
cv.imshow('Equalized Gray', equalized_gray)

# YUV：亮度，色度，饱和度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
# 直方图均衡化yuv[..., 0]也就是[:,:,0]
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
# 将yuv转换为bgr
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equalized Color', equalized_color)
cv.waitKey()