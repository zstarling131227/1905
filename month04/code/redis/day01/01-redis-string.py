import redis

r = redis.Redis('localhost', 6379, 0)
r.set('name', 'xixi')
print(r.get('name'))
r.mset({'age': '23', 'gender': 'F'})
print(r.mget('age', 'gender'))
print(r.strlen('name'))

r.set('age', '23')
print(r.incrby('age', 10))
print(r.decrby('age', 10))
print(r.incr('age'))
print(r.decr('age'))
print(r.incrbyfloat('age', 4))
print(r.incrbyfloat('age', -4))
print(r.get('age'))

r.flushdb()
print(r.get('age'))
print(r.keys('*'))
