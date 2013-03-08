# -*- coding:utf-8 -*-
'''
Created on 2013-3-6
@author: corleone
'''
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request

class Tjyqhdm_Spider(Tjbz_Spider):
    '''
    统计用区划代码和城乡划分代码
    '''
    
    name = "tjyqhdm"

    def parse(self, response):
        
#        hxs = HtmlXPathSelector(response)
#        print hxs.select("//title/text()").extract()[0]
        print response.request.__dict__
#        print response.body.decode('gb2312')
        
        
