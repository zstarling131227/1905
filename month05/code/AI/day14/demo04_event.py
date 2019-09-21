"""
demo04_event.py  案例：事件预测（分类问题，考虑svm）
 svm.SVC做分类
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


# 加载数据
# event.txt（第1列星期做标签编码，第2列日期忽略，第3列时间离散值处理，
# 第4列、第5列进出人数保留‘并且不能做标签编码’，第6列有无事件做标签编码）
# data = np.loadtxt('../ml_data/event.txt', delimiter=',', dtype='U15')
data = np.loadtxt('../ml_data/events.txt', delimiter=',', dtype='U15')
print(data.shape)
# 整理数据集(删除第3列)，1表示删除元素所在行, axis=0表示删除元素所在的列（从左到右删除，列删除）
data = np.delete(data.T, 1, axis=0)
x, y = [], []
encoders = []
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
x=np.array(x).T
y=np.array(y)
print(x.shape,y.shape,x[0],y[0])

# 划分训练集
train_x, test_x, train_y, test_y, = ms.train_test_split(x, y, test_size=0.25, random_state=7)
model = svm.SVC(kernel='rbf',class_weight='balanced')
model.fit(train_x, train_y)
# 针对测试集预测结果 评估分类效果
predict_test_y = model.predict(test_x)
# 准确率
re=(test_y==predict_test_y).sum()/test_y.size
print(re)
print(sm.classification_report(test_y, predict_test_y))
data = [['Tuesday', '13:30:00', '21', '23']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))