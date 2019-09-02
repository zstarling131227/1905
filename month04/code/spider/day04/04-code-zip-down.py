import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1905/11_ajax/day02/ajax_pm1.zip'
auth = ('tarenacode', 'code_2013')
html = requests.get(url, auth=auth).content
filename = url.split('/')[-1]
with open(filename, 'wb') as f:
    f.write(html)
