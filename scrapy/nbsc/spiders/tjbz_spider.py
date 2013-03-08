# -*- coding:utf-8 -*-
'''
Created on 2013-3-6 
@author: corleone
统计标准
'''
from scrapy.spider import BaseSpider

class Tjbz_Spider(BaseSpider):
    name = "nbsc"
    url = "http://www.stats.gov.cn/tjbz/"
    start_urls = [
        "http://www.stats.gov.cn/tjbz/", # 2002-12-31
    ]
    
