"""
demo06_filter 傅里叶频域滤波
"""
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf

# 读文件 采样率（每秒采样个数） 每个采样位移值
sample_rate, sigs = wf.read('../da_data/noised.wav')
sigs = sigs / (2 ** 15)
# sigs /= 2 ** 15
# print(sample_rate)  # 一秒钟采样44100个点
# print(sigs, sigs.shape)  # 采样位移的值

# 绘制音频时域值的：时间/位移图像
times = np.arange(len(sigs)) / sample_rate
mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.grid(linestyle=":")
# mp.plot(times, sigs, color='red', label='Noised Signal')
mp.plot(times[:178], sigs[:178], color='red', label='Noised Signal')
mp.legend()

# 基于傅里叶变换，获取音频频域信息，绘制音频频域的：频率/能量图像。
freqs = nf.fftfreq(sigs.size, 1 / sample_rate)
print(freqs, freqs.shape)
complex_array = nf.fft(sigs)
pows = np.abs(complex_array)
mp.subplot(222)
mp.title('Frequence Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.grid(linestyle=":")
# mp.plot(freqs, pows, color='orangered', label='Noised Freq')
mp.semilogy(freqs[freqs > 0], pows[freqs > 0], color='red', label='Noised Freq')
mp.legend()

# 将低能噪声去除后绘制音频频域的：频率/能量图像。
fun_freq = freqs[pows.argmax()]
# 拿到所有噪声的索引
noised_indices = np.where(freqs != fun_freq)[0]
ca = complex_array.copy()
ca[noised_indices] = 0
filter_pows = np.abs(ca)
mp.subplot(224)
mp.ylabel('pow', fontsize=12)
mp.grid(linestyle=":")
mp.plot(freqs[freqs > 0], filter_pows[freqs > 0], color='red', label='Filter Freq')
mp.legend()

# 基于逆向傅里叶变换，生成新的音频信号，绘制音频时域的：时间/位移图像。
filter_sigs = nf.ifft(ca)
mp.subplot(223)
mp.ylabel('Signal', fontsize=12)
mp.grid(linestyle=":")
mp.plot(times[:178], filter_sigs[:178], color='red', label='Filter Signal')
mp.legend()

# 重新生成音频文件。
filter_sigs = (filter_sigs * (2 ** 15)).astype('i2')
wf.write('../da_data/filter.wav', sample_rate, filter_sigs)

mp.tight_layout()
mp.show()
