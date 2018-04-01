# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 歌手
class WangyiyunArtistItem(scrapy.Item):
    artist_id = scrapy.Field()  # 歌手id
    artist_name = scrapy.Field()  # 歌手姓名
    artist_url = scrapy.Field()  # 歌手链接
    album_url = scrapy.Field()  #

# 专辑list
class WangyiyunAlbumListItem(scrapy.Item):
    album_id = scrapy.Field()
    album_name = scrapy.Field()  # 专辑名称
    each_album_url = scrapy.Field()  #


# 专辑歌曲
class WangyiyunSongItem(scrapy.Item):
    album_name = scrapy.Field()  # 专辑名称
    artist_name = scrapy.Field()  # 歌手
    musicName = scrapy.Field()  # 歌曲名称
    music_url = scrapy.Field()  # 歌曲链接

class WangyiyuncommentItem(scrapy.Item):
    artist_name = scrapy.Field()  # 歌手
    musicName = scrapy.Field()  # 歌曲名称
    comment_no = scrapy.Field()  # 评论数量
    comment_nice = scrapy.Field()  # 热评

