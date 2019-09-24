"""
demo11_news.py  文本分类，主题识别
"""
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import numpy as np

# 5个文件夹，每个文件夹下的文件为样本，其内容为输入x,文件名称为输出y

# shuffle=True随机打乱，random_state=7随机种子
train = sd.load_files('../ml_data/20news', encoding='latin1', shuffle=True, random_state=7)
train_x = np.array(train.data)  # 样本输入（加载所有的文件）
# train.target对文件的名称做标签编码
train_y = np.array(train.target)  # 样本 输出（）
# 类别标签（5个文件夹名称）
cateogries = train.target_names  # 一级目录名
print(train_x.shape, train_y.shape)
print(cateogries)
print(train_x[0])

# 整理样本，获取tfidf矩阵，训练模型
# 获取词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(train_x)
# 获取TF-IDF模型训练器,生成tfidf
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(tfidf.shape)

# 使用基于多项式分布的不素贝叶斯训练模型
model = nb.MultinomialNB()
model.fit(tfidf, train_y)

# 预测
# 测试数据
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
test_bow = cv.transform(test_data)
test_tfidf = tt.transform(test_bow)
pred_y = model.predict(test_tfidf)

for sent, index in zip(test_data, pred_y):
    print(sent, '-->', cateogries[index])
