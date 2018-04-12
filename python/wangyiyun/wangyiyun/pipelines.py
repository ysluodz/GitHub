# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings
from wangyiyun.items import WangyiyunArtistItem, WangyiyunAlbumListItem, WangyiyunSongItem, WangyiyuncommentItem


class WangyiyunPipeline(object):

    def __init__(self):
        # self.filename = open("musicComment.json", "w")

         # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGODB_DBNAME']]  # 获得数据库的句柄
        self.Artist = self.db[settings['MONGODB_COL_ARTIST']]
        self.AlbumList = self.db[settings['MONGODB_COL_ALBUMLIST']]
        self.Song = self.db[settings['MONGODB_COL_SONG']]
        self.Comment = self.db[settings['MONGODB_COL_COMMENT']]

        # self.Artist.remove()
        self.AlbumList.remove()
        # self.Song.remove()
        # self.Comment.remove()
    # 存入mongodb中
    def process_item(self, item, spider):

        # if isinstance(item, WangyiyunArtistItem):
        # #     # text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # #     # self.filename.write(text.encode("utf-8"))
        #     artist_info = dict(item)
        #     self.Artist.insert(artist_info)
        #     return item

        if isinstance(item, WangyiyunAlbumListItem):
            artist_info = dict(item)
            self.AlbumList.insert(artist_info)
            return item

        if isinstance(item, WangyiyunSongItem):
            artist_info = dict(item)
            self.Song.insert(artist_info)
            return item

        if isinstance(item, WangyiyuncommentItem):
            artist_info = dict(item)
            self.Comment.insert(artist_info)
            return item



