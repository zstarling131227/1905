"""
demo01_moviereviews.py 电影评论情感分析
"""

import nltk.classify as cf  # 分类器
import nltk.classify.util as cu  # 语料库
import nltk.corpus as nc  # 评估效果的工具包

"""
要求的数据结构（此示例中是pdata,ndata要求此结构）
    输入 'age': 15, 出现的单词：出现的次数    输出
[ ({'age': 15, 'score1': 95, 'score2': 95}, 'good'),
  ({'age': 15, 'score1': 45, 'score2': 55}, 'bad') ]
"""
# 共2000个样本，1000个正向评论，1000个负向评论

# 整理正向样本
pdata = []
# movie_reviews下pos文件夹内所有文件的路径
fileids = nc.movie_reviews.fileids('pos')
print(fileids)

# words是nc自带的分词器，fileid是路径
print(nc.movie_reviews.words(fileids[1]))
# 输出结果是/home/tarena/nltk_data/corpora/movie_reviews/pos/cv000_29590.txt文件中的所有出现过的单词

for fileid in fileids:
    words = nc.movie_reviews.words(fileid)
    sample = {}
    for word in words:
        sample[word] = True  # 代表当前单词出现过

    pdata.append((sample, 'POSITIVE'))

# 整理负向样本
ndata = []
# movie_reviews下neg文件夹内所有文件的路径
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    words = nc.movie_reviews.words(fileid)
    sample = {}
    for word in words:
        sample[word] = True
    ndata.append((sample, 'NEGATIVE'))

# 整理训练集、测试集以及输入集与输出集
# int防止出现小数
p_size, n_size = \
    int(len(pdata) * 0.8), int(len(ndata) * 0.8)

train_data = pdata[:p_size] + ndata[:n_size]
test_data = pdata[p_size:] + ndata[n_size:]

# 构建nltk自带的朴素贝叶斯分类器，训练模型
model = cf.NaiveBayesClassifier.train(train_data)
# 预测准确度
ac = cu.accuracy(model, test_data)
print('ac:', ac)

# 样本测试
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']

for review in reviews:
    sample = {}
    # split按空格拆分
    words = review.split()
    for word in words:
        sample[word] = True

    pcls = model.classify(sample)
    print(review, '->', pcls)
