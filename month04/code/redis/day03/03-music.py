import redis

r = redis.Redis('localhost', 6379, 0)
r.zadd('song:rank', {'song1': 1, 'song2': 1, 'song3': 1})
r.zadd('song:rank', {'song4': 1, 'song5': 1, 'song6': 1})
r.zincrby('song:rank', 50, 'song1')
r.zincrby('song:rank', 60, 'song6')
r.zincrby('song:rank', 20, 'song5')
# print(r.zscore('song:rank', 'song1'))
# print(r.zrange('song:rank', 0, -1, withscores=True))
# print(r.zrevrange('song:rank', 0, -1, withscores=True), end="")
rank_list = r.zrevrange('song:rank', 0, -1, withscores=True)
i = 0
for rank in rank_list:
    i+=1
    r = rank[1]
    print('第{}名：{},播放次数为:{}'.format(i, rank[0].decode(), r))
