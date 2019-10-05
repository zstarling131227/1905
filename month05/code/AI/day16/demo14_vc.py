"""
demo14_vc.py　视频捕捉
"""
import cv2 as cv

# 报错，因为没有摄像头
# 获取视频捕捉设备
vc = cv.VideoCapture(0)
while True:
    # 读取一帧
    frame = vc.read()[1]
    cv.imshow('VideoCapture', frame)
    # 每个33毫秒，会截图，并且即使不摁键盘方法也会自动退出，
    # 退出键esc的值27，当cv.waitKey()的返回值为27时退出white循环
    if cv.waitKey(33) == 27:
        break
# 释放视频捕捉设备
vc.release()
# 销毁cv的所有窗口
cv.destroyAllWindows()
