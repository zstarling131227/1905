# -*- coding: utf-8 -*-
import json

import scrapy

from ..items import SoItem


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']

    def start_requests(self):
        # for i in range(0,150,30):
        for i in range(5):
            sn = i * 30
            url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'.format(str(sn))
            yield scrapy.Request(
                url=url,
                callback=self.parse_image
            )

    # response是json合适的字符串
    def parse_image(self, response):
        html = json.loads(response.text)
        for img in html['list']:
            item = SoItem()
            item['img_link'] = img['qhimg_url']
            yield item
