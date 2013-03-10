'''
Created on 2013-3-8
@author: corleone
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings


if __name__ == '__main__':
    
    file_name = u"permutation3.json"
    with open(file_name, 'a') as f:
        pass
    
    execute(argv=["scrapy", "crawl", "lottery", "-o%s" % file_name, "-tjsonlines" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation3.lecai_ongoing.settings', {}, {}, [''])))
#    execute(argv=["scrapy", "shell", "http://www.lecai.com/lottery/draw/list/3?lottery_type=3&ds=2000-01-01&de=2013-03-09" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation3_lecai.settings', {}, {}, [''])))
