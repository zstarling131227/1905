from urllib import request

import csv, time, re, random
import pymongo
import pymysql
class MaoyanSpider(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        }
        self.page = 1
        self.db = pymysql.connect('localhost', 'root', '123456', 'maoyandb', charset='utf8')
        self.cursor = self.db.cursor()

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
        self.write_mysql(film_list)

    def write_mysql(self, film_list):
        ins = 'insert into filmset values(%s,%s,%s)'
        data_list=[]
        for film in film_list:
            L=[film[0].strip(),film[1].strip(),film[2].strip()[5:15]]
            data_list.append(L)
        self.cursor.executemany(ins,data_list)
        self.db.commit()


    def main(self):
        # self.get_page('https://maoyan.com/board/4?offset=10')
        for offset in range(0, 91, 10):
            url = self.url.format(str(offset))

            self.get_page(url)
            print('%d页完成' % self.page)
            self.page += 1
            time.sleep(random.randint(1, 3))

        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()
