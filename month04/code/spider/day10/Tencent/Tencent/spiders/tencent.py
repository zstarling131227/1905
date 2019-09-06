# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy_redis.spiders import RedisSpider

from ..items import TencentItem


# class TencentSpider(scrapy.Spider):
# 方法1
# name = 'tencent'
# allowed_domains = ['careers.tencent.com']
# one_url = 'https://careers.tencent.com/tencentcareer/api/' \
#           'post/Query?timestamp=1559294378106&countryId=&' \
#           'cityId=&bgIds=&productId=&categoryId=&parentCategory' \
#           'Id=&attrId=&keyword=&pageIndex={}&pageSize=10&lang' \
#           'uage=zh-cn&area=cn'
# two_url = 'https://careers.tencent.com/tencentcareer/api/post/' \
#           'ByPostId?timestamp=1559&postId={}&language=zh-cn'
# start_urls = [one_url.format(1)]


class TencentSpider(RedisSpider):
    # 方法2
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1559294378106&countryId=&cityId' \
              '=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}' \
              '&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1559&postId={}&language=zh-cn'
    # #项目启动时，阻塞，等待redis发送指令（url）
    redis_key = 'tencent:spider'

    def parse(self, response):
        for page_index in range(1, 51):
            url = self.one_url.format(page_index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one
            )

    def parse_one(self, response):
        html = json.loads(response.text)
        for job in html['Data']['Posts']:
            item = TencentItem()
            item['zh_name'] = job['RecruitPostName']
            item['zh_type'] = job['CategoryName']
            post_id = job['PostId']
            two_url = self.two_url.format(post_id)
            yield scrapy.Request(
                url=two_url,
                meta={'item': item},
                callback=self.parse_two
            )

    def parse_two(self, reponse):
        item = reponse.meta['item']
        html = json.loads(reponse.text)
        item['zh_duty'] = html['Data']['Responsibility']
        item['zh_require'] = html['Data']['Requirement']
        yield item
