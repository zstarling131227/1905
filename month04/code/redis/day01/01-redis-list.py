import redis

r = redis.Redis('localhost', '6379', 0)
# r.lpush('computer', 'pythonweb', 'pybase', 'socket', 'pylist')
# r.linsert('computer', 'before', 'pybase', 'spider')
# print(r.llen('computer'))
# print(r.lrange('computer', 0, -1))
# print(r.rpop('computer'))
print(r.ltrim('computer', 0, 3))
while True:
    res = r.brpop('computer', 1)
    if res:
        print(res)
    else:
        break
print(r.lrange('computer',0,-1))

r.delete('computer')
print(r.keys('*'))
