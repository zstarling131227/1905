import redis

r = redis.Redis('localhost', 6379, 0)
r.flushdb()
r.hset('user1', 'name', 'xixi')
print(r.hget('user1', 'name'))
user_dict = {
    'password': '123456',
    'gender': 'F',
    'height': '165'
}
r.hmset('user1', user_dict)
print(r.hgetall('user1'))
print(r.hkeys('user1'))
print(r.hvals('user1'))
