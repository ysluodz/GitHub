# -*- coding: cp936 -*-
from scrapy.item import Item, Field

class VpoetblogItem(Item):
    # define the fields for your item here like:
    # name = Field()
    article_name = Field() #文章名字
    public_time = Field()  #发表时间
    read_num = Field()     #阅读数量
