# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class Pipeline(object):
    def __init__(self):
        print 'abc'

    def process_item(self, item, spider):
        #Remove invalid data
        #valid = True
        #for data in item:
          #if not data:
            #valid = False
            #raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
            #print 'crawl no data.....\n'
        #if valid:
        #Insert data into txt
        input = open('data.txt', 'a')
        input.write('article_name:'+item['article_name'][0]+'   ')
        input.write('public_time:'+item['public_time'][0]+'   ')
        input.write('read_num:'+item['read_num'][0]+'   ')
        input.close()

        return item
