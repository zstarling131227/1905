"""
demo02_bike.py 随机预侧 （共享单车案例）
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.ensemble as se
import sklearn.utils as su
import sklearn.metrics as sm

# 加载day数据
# 方法1
# data = np.loadtxt('../ml_data/bike_day.csv', dtype='U20', usecols=(), unpack=True, delimiter=',')
# print(data)
# 方法2
header, data = [], []
with open('../ml_data/bike_day.csv', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:  # header
            header = line.split(',')
        else:
            data.append(line.split(','))
        # print(line)

# 整理header与data 即解析输入输出集
header = np.array(header[2:13])
data = np.array(data)
print(data[0])
x = data[:, 2:13].astype('f4')
y = data[:, 15].astype('f4')
print(header)
print(data.shape, x.shape, y.shape)
# # 打乱原始数据集的输入和输出
x, y = su.shuffle(x, y, random_state=7)
# print(x, y)
# 划分训练集和测试集 9:1
train_size = int(len(x) * 0.9)
train_x, text_x, train_y, text_y = x[:train_size], x[:train_size], y[:train_size], y[:train_size]

# 徐阿奴则随机森林模型，训练，预测
model = se.RandomForestRegressor(max_depth=10, n_estimators=1000, min_samples_split=2)
# 使用测试集测试，输出r2_score
model.fit(train_x, train_y)
pred_y = model.predict(text_x)
re = sm.r2_score(text_y, pred_y)
print(re)
random_fi = model.feature_importances_
print(random_fi)

# # 基于决策树的正向激励回归器给出的特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('BIKE FI', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
xs = np.arange(len(random_fi))
sorted_index = random_fi.argsort()[::-1]  # 返回的是排序后的下标
mp.bar(xs, random_fi[sorted_index], color='red', label='BIKE FI')
mp.xticks(xs, header[sorted_index])
mp.legend()
mp.tight_layout()
mp.show()