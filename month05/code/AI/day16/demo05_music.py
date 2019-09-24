"""
demo05_music.py
"""
import scipy.io.wavfile as wf
import json
import numpy as np

with open('../ml_data/12.json') as f:
    freqs = json.loads(f.read())
# 每一个音符及每一个音符的播放时长（也就是音频中的占用时长）
tones = [
    ('G5', 1.5),
    ('A5', 0.5),
    ('G5', 1.5),
    ('E5', 0.5),
    ('D5', 0.5),
    ('E5', 0.25),
    ('D5', 0.25),
    ('C5', 0.5),
    ('A4', 0.5),
    ('C5', 0.75)]
#  采样率
sample_rate = 44100
music = np.empty(shape=1)
print(music.shape)
print('music', music)
for tone, duration in tones:
    times = np.linspace(0, duration, duration * sample_rate)
    print('times.shape', times.shape)
    print(freqs[tone])
    sound = np.sin(2 * np.pi * freqs[tone] * times)
    print('sound.shape', sound.shape)
    music = np.append(music, sound)  # 向矩阵music添加sound值，默认是行添加
    # print(music)
    print('music.shape', music.shape)

music *= 2 ** 15
music = music.astype(np.int16)
wf.write('../ml_data/music.wav', sample_rate, music)
