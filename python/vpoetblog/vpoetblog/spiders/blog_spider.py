# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from vpoetblog.items import VpoetblogItem

class MoiveSpider(CrawlSpider):
    name="vpoetblog"
    allowed_domains=["blog.csdn.net"]
    start_urls=["http://blog.csdn.net/u013018721/article/list/1"]

    rules=[
        Rule(SgmlLinkExtractor(allow=(r'http://blog.csdn.net/u013018721/article/list/\d+'))),
        Rule(SgmlLinkExtractor(allow=(r'http://blog.csdn.net/u013018721/article/details/\d+')), callback="parse_item"),
    ]

    def parse_item(self, response):
        sel = HtmlXPathSelector(response)
        item = VpoetblogItem()
        item['article_name'] = sel.select('//*[@class="link_title"]/a/text()').extract()
        item['public_time'] = sel.select('//*[@class="link_postdate"]/text()').extract()
        item['read_num'] = sel.select('//*[@class="link_view"]/text()').extract()

        return item
