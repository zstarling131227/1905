import redis

r = redis.Redis('localhost', 6379, 0)
key_list=r.keys('*')
for key in key_list:
    print(key.decode())
print(r.type('sp'))
print(r.exists('sp'))

