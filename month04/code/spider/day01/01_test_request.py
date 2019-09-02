
from urllib import request, parse
url='http://www.baidu.com/s?'
headers={'User-Agent':'Mozilla/5.0'}
#发请求获取内容
req=request.Request(url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')
print(html)