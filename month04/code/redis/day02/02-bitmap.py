import redis

r = redis.Redis('localhost', 6379, 0)
r.setbit('user1', 4, 1)
r.setbit('user1', 4, 0)
r.setbit('user1', 6, 1)
r.setbit('user1', 5, 0)
r.setbit('user1', 199, 1)
r.setbit('user2', 99, 1)
r.setbit('user2', 299, 1)
for i in range(1, 366, 2):
    r.setbit('user3', i, 1)
for i in range(1, 366, 3):
    r.setbit('user4', i, 1)
r.setbit('user4', 299, 1)
user_key = r.keys('user*')
print(user_key)
active_user = []
no_active_user = []
for user in user_key:
    print(r.get(user))
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_user.append((user, login_count))
    else:
        no_active_user.append((user, login_count))

print('active_user', active_user)
print('no_active_user', no_active_user)
