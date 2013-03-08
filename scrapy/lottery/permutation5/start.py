'''
Created on 2013-3-8
@author: corleone
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings


if __name__ == '__main__':
    execute(argv=["scrapy", "crawl", "lottery","-opermutation5.json", "-tjsonlines" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation5.settings', {}, {}, [''])))
#    execute(argv=["scrapy", "shell", "http://www.16788.cn/pl3/pl3lshaoma.asp?page=0" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation3.settings', {}, {}, [''])))
