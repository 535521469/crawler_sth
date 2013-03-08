# -*- coding:utf-8 -*-
'''
Created on 2013-3-6 
@author: corleone
统计标准
'''
from scrapy import log
from scrapy.http.request import Request
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider as Base_Spider
from scrapy.nbsc.spiders.tjyqhdm.tjyqhdm_spider import Tjyqhdm_Provincetr_Spider
from scrapy.selector import HtmlXPathSelector

class Tjbz_Spider(Base_Spider):
    
    def parse(self, response):
        '''
        only fetch 统计用区划代码和城乡划分代码
        '''
        
        req_url = response.request.url
        
        from scrapy.nbsc.spiders.xzqhdm.xzqhdm_spider import Xzqhdm_Spider
        
        hxs = HtmlXPathSelector(response)
        a_tags = hxs.select('//table[@bgcolor="#CCCCCC"]/tr/td/a')
        
        urls = []
        with open('crawl_info.cfg', 'r') as f:
            urls = f.readlines()

        urls = map(str.strip, urls)
        
        for a in a_tags:
            year = a.select('text()').extract()[0]
            new_req_url = req_url + a.select('@href').extract()[0]
            
            if new_req_url not in urls:
                yield Request(new_req_url, Tjyqhdm_Provincetr_Spider().parse, cookies={'year':year})
            else:
                log.msg(u' Already Download  -- %s ' % new_req_url)
    
