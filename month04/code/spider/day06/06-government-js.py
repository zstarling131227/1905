import requests
from lxml import etree
import pymysql
import re


class Goverment(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        self.db = pymysql.connect(host='localhost', port=3306, user='root',
                                  password='123456', database='spider6', charset='utf8')
        self.cur = self.db.cursor()

    def get_one_link(self):
        html = requests.get(url=self.url, headers=self.headers).text
        res = etree.HTML(html)
        r_list = res.xpath('//a[@class="artitlelist"]/@href')[1]
        two_level_url = "http://www.mca.gov.cn" + r_list
        return two_level_url

    def get_two_false_link(self):
        html = requests.get(url=self.url, headers=self.headers).content.decode()
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath('//a[@class="artitlelist"]')
        for a in r_list:
            # href=a.xpath('./@href')[0]
            # title=a.xpath('./@title')[0]
            # print(href, title)
            title = a.get('title')
            # print(title)
            re1 = re.findall('.*中华人民共和国县以上行政区划代码', title, re.S)
            # print(re1)
            if re1:
                # two_false_link="http://www.mca.gov.cn" +a.get('href')
                two_false_link = "http://www.mca.gov.cn" + a.get('href')
                # print(two_false_link)
                return two_false_link

    def get_two_real_link(self):
        false_link = self.get_two_false_link()
        html = requests.get(false_link, headers=self.headers).text
        # print(html)
        # with open('response.html', 'w') as f:
        #     f.write(html)
        pattern = re.compile(r'window.location.href="(.*?)";', re.S)
        # real_link = pattern.findall(html) 此时需要的是元素，非列表
        real_link = pattern.findall(html)[0]
        print(real_link)
        sql = 'select * from version where link="{}"'.format(real_link)
        self.cur.execute(sql)
        # print(self.cur.fetchall())
        if self.cur.fetchall():
            # return '数据已经是最新！'  # #return 的值需要打印
            print('数据已经是最新！')
        else:
            self.get_data(real_link)
            sql1 = 'insert into version values(%s)'
            self.cur.execute(sql1, [real_link])
            self.db.commit()
            return '数据已经被存入'

    def get_data(self, real_link):
        print('数据已经被存入')
        html = requests.get(real_link, headers=self.headers).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height="19"]')
        for parse_html1 in tr_list:
            code = parse_html1.xpath('./td[2]/text()')[0]
            city = parse_html1.xpath('./td[3]/text()')[0]
            print(code, city)

    def main(self):
        self.get_two_real_link()
        self.db.close()
        self.cur.close()


if __name__ == '__main__':
    sp = Goverment()
    sp.main()
    # print(sp.get_one_link())
    # print(sp.get_two_false_link())
    # print(sp.get_two_real_link())
