# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    zh_name = scrapy.Field()
    zh_type = scrapy.Field()
    zh_duty = scrapy.Field()
    zh_require = scrapy.Field()
