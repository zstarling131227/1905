# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # scrapy会自动重定向（输出2个）
    # start_urls = ['http://www.baidu.com/']
    # 改为重定向地址（输出1个结果）
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('我是parse函数！')
