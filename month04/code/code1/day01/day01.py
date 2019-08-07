from urllib import request, parse
import time

"""

import urllib.parse
query_string={'wd':'美女'}
result=urllib.parse.urlencode(query_string)
query_string={'wd':'美女','er':'帅哥'}
result=urllib.parse.urlencode(query_string)
print(result)
from urllib import request
from urllib import parse
baseurl='http://www.baidu.com/s?'
headers={'User-Agent':'Mozilla/5.0'}
query_string={'wd':'赵丽颖','pn':'10'}
result=parse.urlencode(query_string)
# print(result)
#拼接url地址
# url=baseurl+result
# url='http://www.baidu.com/s?%s'%result
url='http://www.baidu.com/s?{}'.format(result)
# print(url)
#发请求获取内容
req=request.Request(url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')
print(html)
"""
"""
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
"""
"""
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
"""


# """
# 首页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=0
# 第二页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=50
# 第三页：https://tieba.baidu.com/f?kw=华晨宇吧&pn=100
class BaiduSpider(object):
    def __init__(self):
        # self.headers = {
        #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        # }
        self.headers = {
            'User-Agent' : 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        }
        self.baseurl='https://tieba.baidu.com/f?{}'

    def get_page(self, url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def parse_page(self):
        pass

    def write_page(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    def main(self):
        name = input("输入贴吧名：")
        start = int(input("起始页："))
        end = int(input("终止页："))
        for page in range(start,end+1):
            pn=(page-1)*50
            query_string={
                "kw":name,
                'pn':str(pn)
            }
            query_string=parse.urlencode(query_string)
            url=self.baseurl.format(query_string)
            html=self.get_page(url)
            filename='{}-第{}页.html'.format(name,page)
            self.write_page(filename,html)
            print('第%d页爬取成功'%page)
            time.sleep(1)

if __name__ == "__main__":
    spider = BaiduSpider()
    spider.main()
# """
