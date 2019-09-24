"""
demo07_lc.py   学习曲线(调整训练集与测试集的比例)
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
import sklearn.preprocessing as sp
import sklearn.ensemble as se

# 加载数据
data = np.loadtxt('../ml_data/car.txt', delimiter=',', dtype='U20')
print(data.shape)
train_x, train_y = [], []
encoders = []
data = data.T
for row in range(len(data)):  # 迭代每一列
    # # 标签编码：根据字符串形式的特征值在特征序列中的位置，为其指定一个数字标签，用于提供给基于数值算法的学习模型。
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:  # 说明拿到的是前六列
        train_x.append(encoder.fit_transform(data[row]))
    else:  # 说明拿到的是最后一列
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)

# 整理　训练集的输入与输出
train_x = np.array(train_x).T
train_y = np.array(train_y)
print(train_y.shape)
print(train_x.shape)
print(train_x[0], '　', train_y[0])

# 选择模型，训练模型（根据下面的验证曲线修改参数值）
model = se.RandomForestClassifier(max_depth=9, n_estimators=140, random_state=7)

# 学习曲线
lc_params = np.linspace(0.1, 0.9, 9)
# ms.learning_curve() 中的第四个参数是指需要验证的参数，也就是说经过测试调整出最优值,
# 且learning_curve的返回值是一个元组，包含3个元素，第一个元素用不到，用_去占位置。以测试集位置为主
_, train_x, test_x = ms.learning_curve(model, train_x, train_y, train_sizes=lc_params, cv=5)
print(train_x.mean(axis=1))

# 绘制验证曲线
mp.figure('Validation Curve', facecolor='lightgray')
mp.title('Validation Curve', fontsize=14)
mp.xlabel('train size', fontsize=12)
mp.ylabel('f1_score', fontsize=12)
mp.grid(linestyle=':')
mp.plot(lc_params, test_x.mean(axis=1), 'o-', label='train size')
mp.legend()
mp.show()
