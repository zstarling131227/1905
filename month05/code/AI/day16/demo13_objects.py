"""
demo13_objects.py  图像识别
"""
import os
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl


def search_files(directory):
    '''
    返回如下格式：
    {'car':[url,url....], 'airplane':[url....]}
    '''
    dire = os.path.normpath(directory)
    objects = {}
    # 当前目录  子目录们  文件们
    for curdir, subdirs, files in os.walk(dire):
        for file in files:
            if file.endswith('.jpg'):
                # 当前目录名 作为类别标签
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                # 把path加入到label中
                path = os.path.join(curdir, file)
                objects[label].append(path)
    return objects


train_samples = search_files('../ml_data/objects/training')
# print(train_samples)

# 整理样本数据
train_x, train_y = [], []
for label, filenames in train_samples.items():
    descs = np.array([])
    for filename in filenames:
        # 解析每个文件的特征值矩阵
        img = cv.imread(filename)
        # cvtColor转换颜色，将原图片转换为灰度图像
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 为了避免图片大小带来的影响
        # 对gray进行图像的缩放
        h, w = gray.shape[:2]  # 获取高和宽
        f = 200 / min(h, w)  # 计算缩放比例
        # 等比例缩放，
        cv.resize(gray, None, fx=f, fy=f)
        # 创建特征点检测器
        sift = cv.xfeatures2d.SIFT_create()
        # 拿到特征点
        keypoints = sift.detect(gray)
        # 获取特征值矩阵
        _, desc = sift.compute(gray, keypoints)
        # 把每个文件的desc存入descs
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    train_x.append(descs)
    train_y.append(label)

# 训练隐马模型
# {'car': object, 'airplane': object ...}
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(
        n_components=4, covariance_type='diag',
        n_iter=1000)
    models[label] = model.fit(mfccs)
# 训练了3个model，每个model用于匹配某类图像

# 测试
# 整理测试样本数据
test_x, test_y = [], []
test_samples = \
    search_files('../ml_data/objects/testing')
for label, filenames in test_samples.items():
    descs = np.array([])
    for filename in filenames:
        # 解析每个文件的特征值矩阵
        img = cv.imread(filename)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 对gray进行图像的缩放
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        cv.resize(gray, None, fx=f, fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        # 把每个文件的desc存入descs
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    test_x.append(descs)
    test_y.append(label)

# 模式匹配
pred_y = []
for descs in test_x:  # 遍历3次
    # 验证每个模型对当前desc的匹配度得分
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(descs)
        if (best_score is None) or (best_score < score):
            best_score = score
            best_label = label
    pred_y.append(best_label)

print(test_y)
print(pred_y)
