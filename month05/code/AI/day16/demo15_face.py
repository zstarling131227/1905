"""
demo15_face.py 人脸定位
"""
import cv2 as cv

# 哈尔级联人脸定位器
# 通过特征描述文件构建哈尔级联人脸识别器
fd = cv.CascadeClassifier('../ml_data/haar/face.xml')
ed = cv.CascadeClassifier('../ml_data/haar/eye.xml')
nd = cv.CascadeClassifier('../ml_data/haar/nose.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]  # 第一张人脸
    # 从一个图像中识别出所有的人脸区域
    # 	1.3：为最小的人脸尺寸
    # 	5：最多找5张脸
    # 返回：
    # 	faces: 抓取人脸（矩形区域）列表 [(l,t,w,h),(),()..]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    # faces中存储的的脸的位置， l, t, 表示的是椭圆相对于原始图片的左位移和上位移的距离。 w, h表示的是人脸图片的宽和高
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        # 绘制椭圆（将脸描绘成一个椭圆）
        # ellipse() 原始大图像 椭圆心（相对于图片的大小） 半径（相对于人脸椭圆的大小） 椭圆旋转角度  起始角, 终止角 颜色 线宽
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)

        face = frame[t:t + h, l:l + w]

        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0), 2)

        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 255), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
