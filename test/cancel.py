# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_speeches.py  语音识别
"""
import os
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import hmmlearn.hmm as hl


def search_files(directory):
    '''
    返回如下格式：
    {'apple':[url,url....], 'banana':[url....]}
    '''
    dire = os.path.normpath(directory)
    objects = {}
    # 当前目录  子目录们  文件们
    for curdir, subdirs, files in os.walk(dire):
        for file in files:
            if file.endswith('.wav'):
                # 当前目录名 作为类别标签
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                # 把path加入到label中
                path = os.path.join(curdir, file)
                objects[label].append(path)
    return objects

train_samples = \
    search_files('/home/tarena/zxl/1905/month05/code/AI/ml_data/speeches/training')
# print(train_samples)

# 整理样本数据
train_x, train_y = [], []
for label, filenames in train_samples.items():
    mfccs = np.array([])
    for filename in filenames:
        rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, rate)
        # 把每个文件的mfcc存入mfccs
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    train_x.append(mfccs)
    train_y.append(label)

# 训练隐马模型
# {'apple': object, 'banana': object ...}
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(
        n_components=4, covariance_type='diag',
        n_iter=1000)
    models[label] = model.fit(mfccs)
# 训练了7个model，每个model用于匹配某类声音

# 测试
# 整理测试样本数据
test_x, test_y = [], []
test_samples = \
    search_files('/home/tarena/zxl/1905/month05/code/AI/ml_data/speeches/testing')
for label, filenames in test_samples.items():
    mfccs = np.array([])
    for filename in filenames:
        rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, rate)
        # 把每个文件的mfcc存入mfccs
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    test_x.append(mfccs)
    test_y.append(label)

# 模式匹配
pred_y = []
for mfccs in test_x:  # 遍历7次
    # 验证每个模型对当前mfcc的匹配度得分
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(mfccs)
        if (best_score is None) or (best_score < score):
            best_score = score
            best_label = label
    pred_y.append(best_label)

print(test_y)
print(pred_y)