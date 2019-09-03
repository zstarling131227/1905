# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    # reponse就是baidu 的页面源码

    def parse(self, response):
        print('123456')
        title = response.xpath('/html/head/title/text()')
        print(title)
        #输出的结果为[<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]

        title = response.xpath('/html/head/title/text()').extract()
        # title = response.xpath('/html/head/title/text()').extract_first()
        # title = response.xpath('/html/head/title/text()').get()
        print(title)
        # 输出结果为： ['百度一下，你就知道']
