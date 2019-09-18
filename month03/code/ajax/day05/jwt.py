import jwt

a = jwt.encode({'username': 'xixi'}, '123456', algorithm='HS256')
print(a)
b = jwt.decode(a, '123456', algorithms='HS256')
print(b)

import time

# #40s之后过期，过期后报错
payload = {'username': 'xixi', 'exp': time.time() + 40}
a = jwt.encode(payload, '123456', algorithm='HS256')
print(a)
b = jwt.decode(a, '123456', algorithms='HS256')
print(b)
