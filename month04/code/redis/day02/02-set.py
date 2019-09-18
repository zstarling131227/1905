import redis

r = redis.Redis('localhost', 6379, 1)
r.sadd('myset1', 'A', 'B')
print(r.smembers('myset1'))
print(r.scard('myset1'))
print(r.sismember('myset1', 'A'))
print(r.sismember('myset1', 'C'))
r.sadd('myset4', 'B', 'C')
r.sadd('myset2', 'A', 'B', 'D')
r.sadd('myset3', 'A', 'B', 'C')
print(r.sinter('myset1', 'myset2', 'myset3'))
focus_set = r.sunion('myset1', 'myset2', 'myset3')
set_list = set()
for focus in focus_set:
    focu = focus.decode()
    set_list.add(focu)
print(set_list)
