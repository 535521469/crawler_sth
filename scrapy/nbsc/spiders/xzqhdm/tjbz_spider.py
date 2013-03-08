# -*- coding:utf-8 -*-
'''
Created on 2013-3-6 
@author: corleone
统计标准
'''
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider as Base_Spider
from scrapy import log

class Tjbz_Spider(Base_Spider):
    
    def parse(self, response):
        '''
        '''
        
        req_url = response.request.url
        
        from scrapy.nbsc.spiders.xzqhdm.xzqhdm_spider import Xzqhdm_Spider  
        
        hxs = HtmlXPathSelector(response)
        a_tags = hxs.select('//table//td[@width="94%"]/a')
        
        urls = []
        with open('crawl_info.cfg', 'r') as f:
            urls = f.readlines()

        urls = map(str.strip, urls)
        
        for a in a_tags:
            
            new_req_url = req_url + a.select('@href').extract()[0]
            
            if new_req_url not in urls:
                yield Request(new_req_url, Xzqhdm_Spider().parse)
            else:
                log.msg(u' Already Download  -- %s ' % new_req_url)
    
