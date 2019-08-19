from urllib import request

import csv, time, re, random
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        }
        self.page = 1
        self.conn=pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset =self.db['filmset']

    def get_page(self, url):
        req = request.Request(
            url,
            headers=self.headers
        )
        res = request.urlopen(req)
        html = res.read().decode('utf8')
        self.parse_page(html)

    def parse_page(self, html):
        pattern = re.compile(
            '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        film_list = pattern.findall(html)
        # print(film_list)
        # print(len(film_list))
        self.write_mongo(film_list)

    def write_mongo(self, film_list):
        for film in film_list:
            film_dict={
                '名称':film[0].strip(),
                '主演':film[1].strip(),
                '时间':film[2].strip()
            }
            self.myset.insert_one(film_dict)

    def main(self):
        # self.get_page('https://maoyan.com/board/4?offset=10')
        for offset in range(0, 91, 10):
            url = self.url.format(str(offset))

            self.get_page(url)
            print('%d页完成' % self.page)
            self.page += 1
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()
