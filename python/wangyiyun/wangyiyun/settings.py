# -*- coding: utf-8 -*-

# Scrapy settings for wangyiyun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangyiyun'
# BOT_VERSION = '1.0'

SPIDER_MODULES = ['wangyiyun.spiders']
NEWSPIDER_MODULE = 'wangyiyun.spiders'

ITEM_PIPELINES={
    'wangyiyun.pipelines.WangyiyunPipeline': 300  # 启用一个Item Pipeline组件，数字代表优先级，越小越优先
}

# 连接数据库的信息
MONGODB_HOST='127.0.0.1'
MONGODB_PORT=27017
MONGODB_DBNAME='mydb'
MONGODB_COL_ARTIST = 'ArtistInfo'  # 所有的歌手列表
MONGODB_COL_ALBUMLIST = 'AlbumListInfo'  # 每个歌手的所有专辑列表
MONGODB_COL_COMMENT = 'Comment'  # 每张专辑内的所有歌曲列表
MONGODB_COL_SONG = 'SongInfo'   # 每首歌曲的信息

DOWNLOAD_DELAY = 0.25
# ROBOTSTXT_OBEY = True  # 就是有些不让你爬，有些又允许你爬。默认是True，如果失败了，可以尝试将其注释，然后复制一行，改为False。
ROBOTSTXT_OBEY = False

# IPPOOL=[
#     {"ipaddr":"61.129.70.131:8080"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"120.204.85.29:3128"},
#     {"ipaddr":"219.228.126.86:8123"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"218.82.33.225:53853"},
#     {"ipaddr":"223.167.190.17:42789"}
# ]
# DOWNLOADER_MIDDLEWARES = {
#      # 'myproxies.middlewares.MyCustomDownloaderMiddleware': 543,
#      'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
#      'myproxies.middlewares.MyproxiesSpiderMiddleware': 125
# }

# 从文件读取代理ip
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
    #  'wangyiyun.middlewares.ProxyMiddleWare':125,
    #  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None

    # 'wangyiyun.middlewares.PhantomJSMiddleware': 100
    'wangyiyun.middlewares.JavaScriptMiddleware': 100

}
# PHANTOMJS_PATH = r'/root/phantomjs/bin/phantomjs'


# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
