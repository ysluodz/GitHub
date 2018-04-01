# -*- coding: utf-8 -*-
import json
import pymongo
from scrapy.conf import settings


class TencentPipeline(object):

    def __init__(self):
        # self.filename = open("tencent.json", "w")
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    # 存入json文件
    # def process_item(self, item, spider):
    #     text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.filename.write(text.encode("utf-8"))
    #     return item

    # def close_spider(self, spider):
    #     self.filename.close()

    # 存入mongodb中
    def process_item(self, item, spider):
        article = dict(item)
        self.post.insert(article)
        return item