"""
demo05_movie.py 电影推荐
"""
import json
import numpy as np

with open('../ml_data/ratings.json', 'r') as f:
    rating = json.loads(f.read())

# 所有用户列表
users = list(rating.keys())
scmat = []
# 整理相似度得分矩阵
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        for movie in rating[user1]:
            if movie in rating[user2]:
                movies.add(movie)
        # 两人没有共同看过的电影
        # if len(movies) == 0:
        # 两人共同看过的电影数小于10,
        if len(movies) <= 0:
            score = 0
        else:  # 两人有共同看过的电影,两人相似
            A, B = [], []
            for movie in movies:
                A.append(rating[user1][movie])
                B.append(rating[user2][movie])
            # 计算两人的相似度
            A = np.array(A)
            B = np.array(B)
            # 欧氏距离得分
            # score = np.sqrt(((A - B) ** 2).sum())
            # score = 1 / (1 + score)
            # 皮式距离得分（皮尔逊相关系数）[0,1]表示第一行第2列
            score = np.corrcoef(A, B)[0, 1]
        scrow.append(score)
    scmat.append(scrow)
print(np.round(scmat, 2))

# 召回操作 为每一个人找到所有的推荐电影
# 找到相似用户，按照相似度从高到低排序
scmat = np.array(scmat)
users = np.array(users)
# 枚举遍历
for i, user in enumerate(users):
    # argsort排序后的元素所在原位置的下标
    sorted_indics = scmat[i].argsort()[::-1]
    # 掩码，去掉自身
    sorted_indics = sorted_indics[sorted_indics != i]
    # 掩码 得到相似用户
    sim_users = users[sorted_indics]
    # 掩码 得到相似用户得分
    sim_scores = scmat[i, sorted_indics]
    print(user, sim_users, sim_scores, sep='\n')

    # 生成推荐清单
    pos_mask = sim_scores > 0
    sim_users = sim_users[pos_mask]
    # 使用字典存储最终推荐清单
    # {'哪吒':[9.0, 7.9], '复联4':[8.0, 9.0, 8.0]..}
    recomm_movies = {}
    for i, sim_user in enumerate(sim_users):
        for movie, score in rating[sim_user].items():
            if movie not in rating[user].keys():
                if movie not in recomm_movies:
                    recomm_movies[movie] = [score]
                else:
                    recomm_movies[movie].append(score)
    print('user:')
    print(user)
    # print('recomm_movies:')
    # print(recomm_movies)

    # 针对结果清单进行排序（value的均值)。reverse=True逆序排列
    # 根据均值mean排序
    # movie_list=sorted(recomm_movies.items(),key=lambda x:np.mean(x[1]),reverse=True)
    # 根据加权平均average排序
    movie_list=sorted(recomm_movies.items(),key=lambda x:np.average(x[1]),reverse=True)
    print('movie_list:')
    print(movie_list)