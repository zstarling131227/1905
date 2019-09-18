from urllib import request,parse
headers={
    'User-Agent':''
}
word=input("请输入搜索内容：")
query_string={'wd':word}
query_string=parse.urlencode(query_string)
url='http://www.baidu.com/s?{}'.format(query_string)
req=request.Request(url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')
filename='{}.html'.format(word)
# with open(filename,'w') as f:
with open(filename,'w',encoding='gb18030') as f:
    f.write(html)
# 编码方式
# gbk
# gb2312
# gb18030
# utf-8