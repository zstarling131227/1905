# -*- coding: utf-8 -*-
import scrapy

from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 程序启动时，寻找的第一个地址是start_urls
    # start_urls = ['http://maoyan.com/']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for user in dd_list:
            item = MaoyanItem()
            item['name'] = user.xpath('./a/@title').get()
            item['star'] = user.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = user.xpath('.//p[@class="releasetime"]/text()').extract()[0]
            yield item
        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            yield scrapy.Request(
                url,
                callback=self.parse
            )
