import numpy as np

# 二项分布
print(np.random.binomial(10, 0.7, 1))
print(np.random.binomial(10, 0.7, 10))
a = np.random.binomial(10, 0.7, 100)
print(a)  # 100个数服从二项分布
print((a == 7).sum() / 1000)
for i in range(11):
    print((np.random.binomial(10, 0.7, 10000) == i).sum() / 10000)
print('+' * 100)

# 超几何分布
# 表示在有3个好苹果，4个坏苹果的样本中抽取20次，每次抽取5个，其中是好苹果的数量。
r = np.random.hypergeometric(ngood=3, nbad=4, nsample=5, size=20)  # 表示抽取的20次，有3个好苹果,4个坏的，抽取5个苹果
print(r)
for i in range(7):
    print((np.random.hypergeometric(10, 7, 6, 10000) == i).sum() / 10000)
print('+' * 100)

# 正态分布
r = np.random.normal(10)
print(r)
e = np.random.normal(loc=0, scale=1, size=10)
print(e)
