from urllib import request, parse
import time
import urllib.parse
query_string={'wd':'美女'}
result=urllib.parse.urlencode(query_string)
# query_string={'wd':'美女','er':'帅哥'}
# result=urllib.parse.urlencode(query_string)
print(result)


'''向新浪发起请求,并得到响应内容'''
# 1.导模块
import urllib.request

# 2.向网站发请求,得到响应对象
response = urllib.request.urlopen(
    'https://www.sina.com.cn/',timeout=1
)
# 3.获取响应对象内容(html源码)
html = response.read().decode('utf-8')
# 获取实际数据的URL地址
print(response.geturl())
# 返回HTTP响应码
print(response.getcode())

# encode() : string 转 bytes
# decode() : bytes  转 string


from urllib import request

url = 'http://httpbin.org/get'
response = request.urlopen(url)
# 获取内容
html = response.read().decode('utf-8')
print(html)














