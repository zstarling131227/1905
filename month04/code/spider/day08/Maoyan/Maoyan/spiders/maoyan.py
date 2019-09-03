# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 程序启动时，寻找的第一个地址是start_urls
    # start_urls = ['http://maoyan.com/']
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):
        dd_list=response.xpath()
