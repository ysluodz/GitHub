# -*- coding: cp936 -*-
from scrapy.item import Item, Field

class VpoetblogItem(Item):
    # define the fields for your item here like:
    # name = Field()
    article_name = Field() #��������
    public_time = Field()  #����ʱ��
    read_num = Field()     #�Ķ�����
