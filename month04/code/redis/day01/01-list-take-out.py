import redis
import time
import random

r = redis.Redis('localhost', 6379, 0)
print(r.lrange('url', 0, -1))
for i in range(67):
    url = r.blpop('url', 5)
    if url:
        print(url[1].decode())
    else:
        break
# print(r.lrem('url', 0, 'url_list'))
print(r.lrange('url', 0, -1))
