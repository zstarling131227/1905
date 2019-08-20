from urllib import request
import re
import time
import random

class FilmSkySpider(object):
    def __init__(self):
        self.url=''
        self.headers={
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        }

    def get_page(self,url):
        req=request.Request(
            url,
            headers=self.headers
        )
        res=request.urlopen(req)
        html=res.read().decode('gb18030','ignore')

        return html

    def parse_one_page(self, html):
        pattern=re.compile(r'<table width="100%".*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        film_list=pattern.findall(html)
        # print(film_list)
        for film in film_list:
            name=film[1].strip()
            link='https://www.dygod.net'+film[0].strip()
            download_link=self.get_page(link)
            print(download_link)

    def get_two_page(self,link):
        html=self.get_page(link)
        pattern=re.compile(r'<td style="WORD-WRAP: break-word".*?<a href="(.*?)</td>"',re.S)
        filmlist=pattern.findall(html)
        print(filmlist)
        return pattern.findall(html)[0]


    def parse_two_page(self):
        pass

if __name__ == '__main__':
    # url='https://www.dygod.net/html/gndy/dyzz/index_2.html'
    url='https://www.dygod.net/html/gndy/dyzz/index_2.html'
    spider=FilmSkySpider()
    html=spider.get_page(url)
    spider.parse_one_page(html)