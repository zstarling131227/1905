import hashlib
import base64
import hmac

s = hashlib.sha256()  # 创建sha256对象
s1 = hashlib.sha1()  # 创建sha256对象
s2 = hashlib.md5()  # 创建sha256对象
# word=b'xixi'
word=b'wangbadan'
# word=b'yaoyue'
# word=b'wangning'
# word=b'zhangxingling'
# word = b'I love you.'
# word = b'I like you.'
# word = b'I miss you.'
# word = b'I will be back.'
# word = b'Waiting for you!'
# word = b'Zxl & wn!'
s.update(word)  # 添加欲hash的内容，类型为 bytes
s1.update(word)  # 添加欲hash的内容，类型为 bytes
s2.update(word)  # 添加欲hash的内容，类型为 bytes
s.digest()  # 获取最终结果
s1.digest()  # 获取最终结果
s2.digest()  # 获取最终结果
print(s.digest())
print(s1.digest())
print(s2.digest())

# 生成hmac对象
# 第一个参数为加密的key，bytes类型，
# 第二个参数为欲加密的串，bytes类型
# 第三个参数为hmac的算法，指定为SHA256
h = hmac.new(word, word, digestmod='SHA256')
h.digest()  # 获取最终结果
print(h.digest())

b_s = base64.b64encode(word)
print(b_s)
ss = base64.b64decode(b_s)
print(ss)
