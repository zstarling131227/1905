import json

import requests


class DouBanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

    def get_page(self, params):
        res = requests.get(
            url=self.url,
            params=params,
            headers=self.headers,
            verify=False
        )
        html = res.json()
        self.parse_page(html)

    def parse_page(self, html):
        for film in html:
            name = film['title']
            score = film['score']
            print({'name': name, 'score': score})

    def main(self):
        n = input("输入数量：")
        params = {
            "type": "13",
            "interval_id": "100:90",
            'action': '',
            'start': '0',
            'limit': n,
        }
        self.get_page(params)


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.main()
