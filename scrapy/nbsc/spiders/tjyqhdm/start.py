'''
Created on 2013-3-8
@author: corleone
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings


if __name__ == '__main__':
    with open('crawl_info.cfg','w') as f:
        pass
    execute(argv=["scrapy", "crawl", "nbsc" ], settings=CrawlerSettings(__import__('scrapy.nbsc.spiders.tjyqhdm.settings', {}, {}, [''])))
#    execute(argv=["scrapy", "shell", "http://www.stats.gov.cn/tjbz/cxfldm/2009/index.html" ], settings=CrawlerSettings(__import__('scrapy.nbsc.spiders.tjyqhdm.settings', {}, {}, [''])))
