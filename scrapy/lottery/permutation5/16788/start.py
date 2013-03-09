'''
Created on 2013-3-8
@author: corleone
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings


if __name__ == '__main__':
    
    assert 0 ,u" 质量不过关啊..."
        
    file_name = u"permutation5.json"
    with open(file_name, 'w') as f:
        pass
    
    execute(argv=["scrapy", "crawl", "lottery", "-o%s" % file_name, "-tjsonlines" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation5.16788.settings', {}, {}, [''])))
#    execute(argv=["scrapy", "shell", "http://www.16788.cn/pl3/pl3lshaoma.asp?page=0" ], settings=CrawlerSettings(__import__('scrapy.lottery.permutation3.settings', {}, {}, [''])))
