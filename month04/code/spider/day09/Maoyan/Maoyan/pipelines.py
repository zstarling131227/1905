# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from .settings import *


class MaoyanPipeline(object):

    def process_item(self, item, spider):
        # print(item['name'])
        # print(item['star'])
        # print(item['time'])
        return item


class MaoyanMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            # port=MYSQL_PORT,
            charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
        print('我是open_spider函数')

    def process_item(self, item, spider):
        ins = 'insert into filmtab values(%s, %s, %s)'
        film_list = [
            item['name'], item['star'], item['time']
        ]
        # print(film_list)
        self.cursor.execute(ins, film_list)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        print('我是close_spider函数')


class MaoyanMongoPipeline(object):
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT
        )
        self.db = self.conn['maoyandb']
        self.myset = self.db['filmtab1']
        print('我是open_spider函数')

    def process_item(self, item, spider):
        film_dict = {
            'name': item['name'],
            'star': item['star'],
            'time': item['time'],
        }
        # print(film_dict)
        self.myset.insert_one(film_dict)

        # 必须写,此函数返回值会交给下一个管道继续处理item数据（下一个是由settings中的优先级决定的）
        return item

    def close_spider(self, spider):
        print('我是close_spider函数')
