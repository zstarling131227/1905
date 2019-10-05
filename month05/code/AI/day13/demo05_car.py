"""
demo05_car.py 随机森林分类器 小汽车评级
"""
# 案例：基于决策树分类算法训练模型预测小汽车等级。

# 1. 读取文本数据，对每列进行标签编码，基于随机森林分类器进行模型训练，进行交叉验证。
import numpy as np
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
# 选择模型，训练模型
model = se.RandomForestClassifier(max_depth=9, n_estimators=140, random_state=7)
# 交叉验证
cv = ms.cross_val_score(model, train_x, train_y, cv=5, scoring='accuracy')
print(cv)
print(cv.mean())
model.fit(train_x, train_y)

# 　客户端传递来一组样本，每个样本给出预测结果（正常来讲是只有前六列，但是为了方便验证预测结果，给出了第七列）
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]

data = np.array(data).T

# 使用训练时创建的LabelEncoder（也就是encoders[]）处理样本输入
text_x, text_y = [], []
for row in range(len(data)):  # 迭代每一列
    if row < len(data) - 1:  # 说明拿到的是前六列
        text_x.append(encoders[row].transform(data[row]))
    else:  # 说明拿到的是最后一列
        text_y = encoders[row].transform(data[row])
# 使用model对测试样本进行预测
text_x = np.array(text_x).T
pred_test_y = model.predict(text_x)
print(text_y, pred_test_y)
# 使用最后一个LabelEncoder转换输出
print(encoders[-1].inverse_transform(text_y))
print(encoders[-1].inverse_transform(pred_test_y))
