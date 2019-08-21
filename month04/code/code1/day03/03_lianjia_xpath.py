import requests
import time, random
from lxml import etree


class LianJiaSpider(object):
    def __init__(self):
        self.url = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        }
        self.page = 1

    def get_page(self, url):
        res = requests.get(
            url,
            headers=self.headers
        )
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    ##用xpath数据提取
    def parse_page(self, html):
        pass

    def main(self):
        # self.get_page('https://maoyan.com/board/4?offset=10')
        for offset in range(0, 31, 10):
            url = self.url.format(str(offset))

            self.get_page(url)
            print('%d页完成' % self.page)
            self.page += 1
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.main()
