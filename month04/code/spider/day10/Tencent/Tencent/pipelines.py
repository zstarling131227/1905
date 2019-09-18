# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TencentPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(
            # root用户只能可连接本地
            '127.0.0.1', 'root', '123456', 'tencentdb', charset='utf8'
            # 其他用户可以用IP链接
            # '176.23.4.102', 'xxx(mysql 用户)', '123456', 'tencenttab', charset='utf8'
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into tencenttab values(%s,%s,%s,%s)'
        job_list = [
            item['zh_name'], item['zh_type'], item['zh_duty'],
            item['zh_require']
        ]
        self.cursor.execute(ins, job_list)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
