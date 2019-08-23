import requests
import time, random
from lxml import etree


class LianJiaSpider(object):
    def __init__(self):
        self.url = "https://hz.lianjia.com/ershoufang/pg{}/"
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
        parse_html = etree.HTML(html)
        li_list = parse_html.xpath('//*[@id="content"]/div[1]/ul/li')
        # print(li_list)
        for li in li_list:
            name = li.xpath('.//div[@class="houseInfo"]/a/text()')[0].strip()
            total_price = li.xpath('.//div[@class="totalPrice"]/span[1]/text()')[0].strip()
            unit_price = li.xpath('.//div[@class="unitPrice"]/span[1]/text()')[0].strip()
            # print(name)
            # print(total_price)
            # print(unit_price)

            house_dict = {
                'name': name,
                'total_price': total_price,
                'unit_price': unit_price,
            }
            print(house_dict)
        print(len(li_list))

    def main(self):
        # self.get_page('https://maoyan.com/board/4?offset=10')
        for pg in range(1, 2):
            url = self.url.format(str(pg))

            self.get_page(url)
            print('%d页完成' % self.page)
            self.page += 1
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.main()
