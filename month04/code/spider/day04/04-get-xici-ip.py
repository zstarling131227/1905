from lxml import etree
from fake_useragent import UserAgent
import requests
import random

# （有问题）

class Spider(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com'
        self.proxies_list = []

    def get_random_ua(self):
        ua = UserAgent()
        print(ua.random)
        return ua.random

    def get_ip_list(self):
        html = requests.get(
            self.url,
            headers={
                'User-Agent': self.get_random_ua()
            }
        ).text
        parse_html = etree.HTML(html)
        # tr_list = parse_html.xpath('//tbody/tr')
        tr_list = parse_html.xpath('//*[@id="ip_list"]/tbody//tr[@class="odd"]')
        print(tr_list)
        for tr in tr_list[1:]:
            # ip = tr.xpath('./td[2]/text()')
            ip = tr.xpath('//*[@id="ip_list"]/tbody/tr/td[2]/text()')
            print(ip)
            # port = tr.xpath('./td[3]/text()')
            port = tr.xpath(' //*[@id="ip_list"]/tbody/tr/td[3]/text()')
            print(port)
            proxies = {
                'http': 'http://{}:{}'.format(ip, port),
                'https': 'https://{}:{}'.format(ip, port)
            }
            self.proxies_list.append(proxies)


if __name__ == '__main__':
    spider = Spider()
    spider.get_ip_list()
    print(spider.proxies_list)
