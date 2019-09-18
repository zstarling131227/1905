from urllib import request,parse


# string='王八蛋'
# print(parse.quote(string))
# url='http://www.baidu.com/s?wd=%s'%parse.quote(string)

headers={
    'User-Agent':''
}
word=input("请输入搜索内容：")
query_string=parse.quote(word)
url='http://www.baidu.com/s?wd={}'.format(query_string)
req=request.Request(url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')
filename='{}.html'.format(word)
with open(filename,'w',encoding='gb18030') as f:
    f.write(html)
