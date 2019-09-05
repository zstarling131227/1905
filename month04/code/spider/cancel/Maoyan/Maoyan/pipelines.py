# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])

        return item

import pymysql
from .settings import *
# 定义一个MySQL管道类
class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        # 爬虫程序启动时,只执行一次,一般用于建立数据库连接
        self.db = pymysql.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            password = MYSQL_PWD,
            database = MYSQL_DB,
            charset = MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
        print('我是open_spider函数')

    def process_item(self,item,spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        film_list = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(ins,film_list)
        self.db.commit()

        # 必须写,此函数返回值会交给下一个管道继续处理item数据
        return item

    def close_spider(self,spider):
        # 爬虫程序结束时,只执行一次,一般用于断开数据库连接
        self.cursor.close()
        self.db.close()
        print('我是close_spider函数')

import pymongo

class MaoyanMongoPipeline(object):
    def open_spider(self,spider):
        # 连接对象
        self.conn = pymongo.MongoClient(
            host = MONGO_HOST,
            port = MONGO_PORT
        )
        # 库对象
        self.db = self.conn['maoyandb']
        # 集合(表)对象
        self.myset = self.db['filmtab']

    def process_item(self,item,spider):
        film_dict = {
            '电影名称':item['name'],
            '电影主演':item['star'],
            '上映时间':item['time'],
        }
        self.myset.insert_one(film_dict)

        return item
















