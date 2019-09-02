import hashlib
import base64
import hmac

s = hashlib.sha256()  # 创建sha256对象
word = b'xixi'
s.update(word)  # 添加欲hash的内容，类型为 bytes
s.digest()  # 获取最终结果
print(s.digest())

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
