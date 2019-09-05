# -*- coding: utf-8 -*-
import scrapy

from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan3'
    allowed_domains = ['maoyan.com']
    offset = 0

    def start_requests(self):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse_html
            )

    def parse_html(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for user in dd_list:
            item = MaoyanItem()
            item['name'] = user.xpath('./a/@title').get()
            item['star'] = user.xpath('.//p[@class="star"]/text()').extract()[0].strip()
            item['time'] = user.xpath('.//p[@class="releasetime"]/text()').extract()[0]
            yield item
