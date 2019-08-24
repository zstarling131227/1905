from hashlib import md5,sha1

string = 'wangbadan'

# s = md5()
s = sha1()
s.update(string.encode())
result = s.hexdigest()
print(result)
