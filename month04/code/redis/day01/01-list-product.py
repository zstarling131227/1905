import redis
import time
import random

r = redis.Redis('localhost', 6379, 0)
for i in range(67):
    url_list = 'http%d' % i
    r.lpush('url', url_list)
    time.sleep(random.randint(1, 3))
print(r.lrange('url', 0, -1))
