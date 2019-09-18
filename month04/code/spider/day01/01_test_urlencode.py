from urllib import request
from urllib import parse
baseurl='http://www.baidu.com/s?'
headers={'User-Agent':'Mozilla/5.0'}
query_string={'wd':'赵丽颖','pn':'10'}
result=parse.urlencode(query_string)
print(result)
#拼接url地址
url=baseurl+result
# url='http://www.baidu.com/s?%s'%result
# url='http://www.baidu.com/s?{}'.format(result)
print(url)