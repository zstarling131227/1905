import redis

r = redis.Redis('localhost', 6379, 0)
day01_dict = {
    'huawei': 5000,
    'oppo': 4000,
    'iphone': 3000
}
day02_dict = {
    'huawei': 5200,
    'oppo': 4300,
    'iphone': 3230
}
day03_dict = {
    'huawei': 5500,
    'oppo': 4400,
    'iphone': 3600
}
r.zadd('mobile-001', day01_dict)
print(r.zrange('mobile-001', 0, -1))
r.zadd('mobile-002', day02_dict)
print(r.zrange('mobile-002', 0, -1))
r.zadd('mobile-003', day03_dict)
print(r.zrange('mobile-003', 0, -1))

print(r.zunionstore('mobile:001-003', ('mobile-001', 'mobile-002', 'mobile-003'), aggregate='max'))
rank_list = r.zrevrange('mobile:001-003', 0, 2, withscores=True)
print(rank_list)
i = 0
for rank in rank_list:
    i += 1
    print('排名第{}的{}销量为{}'.format(i, rank[0].decode(), int(rank[1])))
