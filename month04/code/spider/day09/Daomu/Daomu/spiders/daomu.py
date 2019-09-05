# -*- coding: utf-8 -*-
import scrapy

from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        link_list = response.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        for link in link_list:
            yield scrapy.Request(
                url=link,
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
        article_list = response.xpath('//article')
        for article in article_list:
            item = DaomuItem()
            info_list = article.xpath('./a/text()').get().split()
            item['volume_name'] = info_list[0]
            item['zh_num'] = info_list[1]
            item['zh_name'] = info_list[2]
            item['zh_link'] = article.xpath('./@href').get()
            yield scrapy.Request(
                url=item['zh_link'],
                meta={'item', item},
                callback=self.parse_three_html
            )

    def parse_three_html(self, response):
        item = response.meta['item']
        # 不可以用extract_first或者get,
        content_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        # 因为内容很多
        item['zh_content'] = '\u3000\u3000'.join(content_list)
        yield item
