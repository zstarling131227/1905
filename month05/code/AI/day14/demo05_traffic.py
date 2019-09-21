"""
demo05_traffic.py  案例：交通流量预测（回归问题）（考虑svm,和决策树两种方法）
 svm.SVR做回归
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.model_selection as ms


class DigitEncoder():
    # 模拟LabelEncoder自定义的数字编码器
    def fit_transform(self, y):
        return y.astype('i4')

    def transform(self, y):
        return y.astype('i4')

    def inverse_transform(self, y):
        return y.astype('str')


# 加载数据 traffic.txt
# 第1列星期，第2列时间离散值处理，第3列队伍所属归家，第4列该队伍是否领先。
# 前四列做标签编码。作为输入
# 第5列5分钟内车流量，作为输出
data = np.loadtxt('../ml_data/traffic.txt', delimiter=',', dtype='U15')
print(data.shape)
# 整理数据集
x, y = [], []
encoders = []
data=data.T
for row in range(len(data)):
    # 确定当前这组特征使用何种编码器
    if data[row][0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    #
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
y = np.array(y)
print(x.shape, y.shape, x[0], y[0])

# 划分训练集
train_x, test_x, train_y, test_y, = ms.train_test_split(x, y, test_size=0.25, random_state=7)
# epsilon=0.2表示2条支持向量之间的间距。
# 2条支持向量之间的样本距离显示为0，拟合的是两条支持向量机之外的点
model = svm.SVR(kernel='rbf', C=10, epsilon=0.2)
model.fit(train_x, train_y)
# 针对测试集预测结果 评估分类效果
predict_test_y = model.predict(test_x)
# r2_score
print(sm.r2_score(test_y, predict_test_y))
print(sm.mean_absolute_error(test_y, predict_test_y))


data = [['Tuesday', '13:35', 'San Francisco', 'yes']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(pred_y)