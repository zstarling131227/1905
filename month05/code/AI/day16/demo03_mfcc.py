"""
demo03_mfcc.py mfcc矩阵
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf
import numpy.fft as nf
import python_speech_features as sf
import hmmlearn.hmm as hl

# 读取音频的mfcc矩阵
sample_rate, sigs = wf.read('../ml_data/speeches/training/apple/apple01.wav')
print(sample_rate, sigs.shape)
# 提取mfcc矩阵
mfcc = sf.mfcc(sigs, sample_rate)
mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.show()
