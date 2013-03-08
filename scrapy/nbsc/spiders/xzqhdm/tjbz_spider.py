# -*- coding:utf-8 -*-
'''
Created on 2013-3-6 
@author: corleone
统计标准
'''
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider as Base_Spider

class Tjbz_Spider(Base_Spider):
    
    def parse(self, response):
        '''
        '''
        from scrapy.nbsc.spiders.xzqhdm.xzqhdm_spider import Xzqhdm_Spider  
        
        hxs = HtmlXPathSelector(response)
        a_tags = hxs.select('//table//td[@width="94%"]/a')
        
        modify_dict = {}
        
        for a in a_tags:
            modify_dict[a.select('@href').extract()[0]] = a.select('text()').extract()[0]
            yield Request(response.request.url + a.select('@href').extract()[0], Xzqhdm_Spider().parse)
            
    
