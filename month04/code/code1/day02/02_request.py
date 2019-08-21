from urllib import request
import requests
url='http://www.baidu.com/'
headers={
    'User-Agent':'Mpzilla/5.0'
}
res=requests.get(url,headers=headers)
print(type(res.text))
# print(res.encoding)
res.encoding='utf-8'
print(type(res.content))
print(res.status_code)
print(res.url)