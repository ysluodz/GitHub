# Scrapy settings for vpoetblog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'vpoetblog'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['vpoetblog.spiders']
NEWSPIDER_MODULE = 'vpoetblog.spiders'

ITEM_PIPELINES={
    'vpoetblog.pipelines.Pipeline': 300
}


DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True


