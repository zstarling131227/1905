"""
demo05_fft.py 傅里叶变换 拆解方波
"""
import numpy.fft as nf
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.zeros(1000)
n = 1000
for i in range(1, n + 1):
    y += 4 / ((2 * i - 1) * np.pi) * np.sin((2 * i - 1) * x)
# for i in range(1, 4):
#     y_ = 4 / ((2 * i - 1) * np.pi) * np.sin((2 * i - 1) * x)
#     mp.plot(x, y_, alpha=0.5)
#     y += y_

# 针对这组曲线数据，执行fft操作
complex_array = nf.fft(y)  # 拆 每一个复数元素代表一个正弦曲线
# print(complex_array)
y_ = nf.ifft(complex_array)
mp.subplot(121)
mp.plot(x, y, label='n=1000')
mp.plot(x, y_, label='ifft', linewidth=7, color='blue', alpha=0.5)

# 绘制频域图像，水平轴表示fft后所有正弦曲线的频率
# 垂直轴表示fft后所有正弦曲线的能量
# 采样数量，采样周期
freqs = nf.fftfreq(y.size, x[1] - x[0])
pows = np.abs(complex_array)  # 求模
mp.subplot(122)
# mp.plot(freqs, pows, color='red')
mp.plot(freqs[freqs > 0], pows[freqs > 0], color='red')

mp.legend()
mp.show()
