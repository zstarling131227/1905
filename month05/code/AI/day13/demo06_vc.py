"""
demo06_vc.py validation_curve.py 验证曲线
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

# 交叉验证不做，做验证曲线
# ms.validation_curve() 中的第四个参数是指需要验证的参数，也就是说经过测试调整出最优值
n_estimators_params = np.arange(100, 200, 10)  # 验证n_estimators参数（确定的最优值是140）
# train_x, test_x = ms.validation_curve(model, train_x, train_y, 'n_estimators', n_estimators_params, cv=5)
max_depth_params = np.arange(1, 11)  # 验证max_depth参数（确定的最优值是9）
train_x, test_x = ms.validation_curve(model, train_x, train_y, 'max_depth', max_depth_params, cv=5)
# print(train_x)
print(train_x.mean(axis=1))

# 绘制曲线
mp.figure('Validation Curve', facecolor='lightgray')
mp.title('Validation Curve', fontsize=14)
# mp.xlabel('n_estimators', fontsize=12)
mp.xlabel('max_depth', fontsize=12)
mp.ylabel('f1_score', fontsize=12)
mp.grid(linestyle=':')
# mp.plot(n_estimators_params, test_x.mean(axis=1), 'o-',label='Validation Curve')
mp.plot(max_depth_params, test_x.mean(axis=1), 'o-', label='max_depth')
mp.legend()
mp.show()
