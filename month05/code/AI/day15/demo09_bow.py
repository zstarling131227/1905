"""
demo09_bow.py 词袋模型
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
# 拆分3个句子，每个句子为一个样本
sentences = tk.sent_tokenize(doc)
print(sentences)
# 构建词袋模型对象
cv = ft.CountVectorizer()
# 训练模型，把句子中所有可能出现的单词作为特征名，
# 每一个句子为一个样本，单词在句子中出现的次数为特征值。
bow = cv.fit_transform(sentences).toarray()
print(bow)
print(bow.toarray())  # 输出为稀疏矩阵
print(cv.get_feature_names())  # 输出为特征名称
# 获取所有特征名
words = cv.get_feature_names()
print(words)
