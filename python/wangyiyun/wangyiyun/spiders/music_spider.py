# -*- coding: utf-8 -*-
from lxml import etree
import scrapy
import re
from scrapy.crawler import CrawlerProcess
from scrapy.selector import HtmlXPathSelector
from selenium.webdriver.remote import switch_to
from wangyiyun.items import WangyiyunArtistItem, WangyiyunAlbumListItem, WangyiyunSongItem, WangyiyuncommentItem


class WangyiyunSpider(scrapy.Spider):

    name = "wangyiyun"
    allowed_domain = ['http://music.163.com']
    group_ids = (1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003)
    initials = [i for i in range(65, 91)] + [0]  # 歌手首字母id
    headers = {
            "Referer":"http://music.163.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
    }

    # def __init__(self, driver):
    #     pass


    def start_requests(self):
        for gid in self.group_ids:
            for initial in self.initials:
                # url = 'http://music.163.com/discover/artist/cat?id={gid}&initial={initial}'.format(gid=gid, initial=initial)
                # yield scrapy.Request(url=url, headers=self.headers, method='GET', callback=self.parse)



                # url = 'http://music.163.com/artist/album?id=6452&limit=3&offset=0'
                url2 = 'http://music.163.com/artist/album?id=3691&limit=100&offset=0'  #
                # url3 = 'http://music.163.com/album?id=34720827'
                # url4 = 'http://music.163.com/song?id=29947420'  # fade
                # # yield scrapy.Request(url=url, headers=self.headers, method='GET', callback=self.parse)
                yield scrapy.Request(url=url2, headers=self.headers, method='GET', callback=self.parse_album)
                # yield scrapy.Request(url=url4, headers=self.headers, method='GET', callback=self.parse_song)
                # request = scrapy.Request(url=url3, headers=self.headers, method='GET', callback=self.parse_album_song)


    # 歌手 1
    def parse(self, response):
        lis = response.xpath('//ul[@id="m-artist-box"]/li').extract()
        for li in lis:
            li = etree.HTML(li)
            artist_name = li.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/text()')[0]
            post_url = li.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@href')[0]   # li <a href=" /artist?id=1876" class="nm nm-icn f-thide s-fc0" title="阿杜的音乐">阿杜</a>

            print '歌手 1----------------歌手:', artist_name
            item = WangyiyunArtistItem()
            p_url = post_url.lstrip()  # 去首尾空格 /artist?id=1876
            album_url = p_url.split('?')   # /artist,id=1876

            item['artist_id'] = int(re.compile(r'\d+').findall(p_url)[0])
            item['artist_name'] = artist_name
            item['artist_url'] = 'http://music.163.com' + p_url  # http://music.163.com/#/artist?id=1876
            item['album_url'] = 'http://music.163.com' + album_url[0] + '/album?' + album_url[1]  # http://music.163.com/#/artist/album?id=1876

            yield item

            album_url_new = item['album_url'] + '&limit=100&offset=0'   # url = 'http://music.163.com/artist/album?id=1876&limit=100&offset=0'
            yield scrapy.Request(url=album_url_new, headers=self.headers, method='GET', callback=self.parse_album)

    # 专辑 2
    def parse_album(self, response):
        lis = response.xpath('//ul[@id="m-song-module"]/li').extract()   # <a href="/album?id=35450297" class="tit s-fc0">烂好人</a>
        for li in lis:
            item = WangyiyunArtistItem()
            li = etree.HTML(li)
            album_name = li.xpath('//a[@class="tit s-fc0"]/text()')[0]
            post_url = li.xpath('//a[@class="tit s-fc0"]/@href')[0]

            item = WangyiyunAlbumListItem()
            p_url = post_url.lstrip()  # /album?id=35450297

            item['album_id'] = long(re.compile(r'\d+').findall(p_url)[0])
            # item['artist_name'] = artist_name
            item['album_name'] = album_name
            item['each_album_url'] = 'http://music.163.com' + p_url

            print '专辑名：', album_name, item['each_album_url']

            yield item

            yield scrapy.Request(url=item['each_album_url'], headers=self.headers, method='GET', callback=self.parse_album_song)


    # 专辑里的歌曲 3
    def parse_album_song(self, response):
        trs = response.xpath('//tbody/tr').extract()
        # print trs.extract()
        album_name = response.xpath('//div[@class="tit"]/h2[@class="f-ff2"]/text()').extract()[0]
        artist_name = response.xpath('//a[@class="s-fc7"]/text()').extract()[0]
        print '专辑:', album_name,  '歌手:', artist_name
        for tr in trs:
            item = WangyiyunSongItem()
            tr = etree.HTML(tr)
            musicName = tr.xpath('//span[@class="txt"]/a/b/@title')[0]
            music_url = tr.xpath('//a/@href')[0]

            print '歌曲名:', musicName,  '歌曲URL:', music_url

            item['album_name'] = album_name
            item['artist_name'] = artist_name
            item['musicName'] = musicName
            item['music_url'] = 'http://music.163.com' + music_url

            yield item

            yield scrapy.Request(url=item['music_url'], headers=self.headers, method='GET', callback=self.parse_song)



     # 歌曲评论 4
    def parse_song(self, response):
        item = WangyiyuncommentItem()
        musicName = response.xpath('//div[@class="tit"]/em[@class="f-ff2"]/text()').extract()[0]
        artist_name = response.xpath('//p[@class="des s-fc4"]/span/a[@class="s-fc7"]/text()').extract()[0]
        comment_no = response.xpath('//div[@class="u-title u-title-1"]/span/span[@class="j-flag"]/text()').extract()[0]
        comment = []

        comments = response.xpath('//div[@class="cmmts j-flag"]/div').extract()
        for comment_each in comments:
            comment_each = etree.HTML(comment_each)
            per_comment_all = []
            per_comment_usr = comment_each.xpath('//a[@class="s-fc7"]/text()')[0]  # 评论者
            per_comment_content = comment_each.xpath('//div[@class="cnt f-brk"]/text()')[0]  # 评论内容
            per_comment_zanNo = comment_each.xpath('//a[@data-type="like"]/text()')[0]  # 点赞人数

            per_comment_all.append(per_comment_usr)
            per_comment_all.append(per_comment_content)
            per_comment_all.append(per_comment_zanNo)

            comment.append(per_comment_all)

            if len(comment) == 10:
                break
        item['musicName'] = musicName
        item['artist_name'] = artist_name
        item['comment_no'] = comment_no
        item['comment_nice'] = comment

        yield item