"""
demo10_tfidf.py  词频-逆文档频率(TF-IDF)
"""
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import numpy as np

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
# 获取词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
# 生成tfidf
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
tfidf = np.round(tfidf.toarray(), 2)
print(tfidf)
