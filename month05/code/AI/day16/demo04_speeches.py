"""
demo04_speeches.py 语音识别
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf
import numpy.fft as nf
import python_speech_features as sf
import hmmlearn.hmm as hl
import os

# os.path.sep是指操作系统级别的分隔符
print('os.path.sep', os.path.sep)


def search_files(directory):
    '''
        返回如下格式：
        {'apple':[url,url....], 'banana':[url....]}
    '''
    # 把当前路径的分隔符转成符合当前操作系统的分隔符，例如将window下的\转为Linux下的/
    directory = os.path.normpath(directory)
    objects = {}
    # 当前目录 子目录们 文件们
    # 递归获得文件名
    for curdir, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                # 获取当前目录名作为类别标签

                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                # 把path加入到label中
                path = os.path.join(curdir, file)
                # print(path)
                # 输出结果：../ml_data/speeches/training/pineapple/pineapple10.wav

                # 把当前目录跟当前文件名拼接
                objects[label].append(path)
    return objects


train_samples = search_files('../ml_data/speeches/training')
# print(train_samples)
'''
# 输出结果是：{文件夹名1：[文件名1，文件名2，...],文件夹名2：[文件名1，文件名2，...],...}
 {
 'pineapple': ['../ml_data/speeches/training/pineapple/pineapple10.wav',
 ...,
 '../ml_data/speeches/training/pineapple/pineapple12.wav'],
 ...,
 'lime': ['../ml_data/speeches/training/lime/lime13.wav',
  ...,
  '../ml_data/speeches/training/lime/lime04.wav']
 }

'''
# 整理样本数据
train_x, train_y = [], []
for label, filenames in train_samples.items():
    mfccs = np.array([])
    for filename in filenames:
        rate, sigs = wf.read(filename)
        # print(rate, sigs)
        # 输出结果：8000 [  70   19  -34 ... -176 -120 -110]
        mfcc = sf.mfcc(sigs, rate)
        # 把每个文件的mfcc存入mfccs
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
            # print('mfccs', mfccs)
    train_x.append(mfccs)
    train_y.append(label)

# 训练隐马模型
# {'apple': object, 'banana': object ...}
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=1000)
    models[label] = model.fit(mfccs)

# 训练了7个model，每个model用于匹配某一类声音

# 整理测试样本数据
test_x, test_y = [], []
test_samples = search_files('../ml_data/speeches/testing')
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
    test_x.append(mfccs)
    test_y.append(label)

# 模式匹配
pred_y = []
for mfccs in test_x:
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
