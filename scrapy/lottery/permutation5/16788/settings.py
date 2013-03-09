# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
BOT_NAME = 'lottery'

SPIDER_MODULES = ['scrapy.lottery.permutation5.16788.permutation5spider']
#NEWSPIDER_MODULE = 'scrapy.statsgov.spiders'

LOG_LEVEL=u"INFO"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
