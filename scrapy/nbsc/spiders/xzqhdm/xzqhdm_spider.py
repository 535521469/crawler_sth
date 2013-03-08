# -*- coding:utf-8 -*-
'''
Created on 2013-3-7 
@author: corleone
'''
from scrapy.http.request import Request
from scrapy.nbsc.spiders.tjbz_spider import Tjbz_Spider
from scrapy.nbsc.spiders.xzqhdm.items import XzqhdmItemLoader, XzqhdmItem
from scrapy.selector import HtmlXPathSelector
import datetime
import hashlib
import os.path
import re
from scrapy.contrib.exporter import JsonLinesItemExporter
import itertools
import string

class Xzqhdm_Spider(Tjbz_Spider):
    '''
    县及县以上行政区划代码
    '''
    
    name = "xzqhdm"

    def parse(self, response):

        req_url = response.request._url

        hxs = HtmlXPathSelector(response)
        title = hxs.select("//title/text()").extract()[0]
        enddate = title[title.find(u"（") + 3:title.find(u"）")]
        meta_content = hxs.select('//head/meta/@content').extract()[0]
        
        m = hashlib.md5()
        m.update(response.body)
        code = m.hexdigest()
        
        if meta_content.find('text/html') > -1:
            file_suffix = "html"
        
        if not os.path.exists(enddate):
            os.mkdir(enddate)
        
        with open(enddate + u"/" + title + u"." + file_suffix, 'wb') as f:
            f.write(response.body)
        
        trs = hxs.select('//span[@class="content"]/table/tbody/tr')
        items = []
        
        for tr in trs:
            i = XzqhdmItemLoader(XzqhdmItem())
            code = tr.select("td[1]/p/span/text()").extract()[0]
            label = tr.select("td[2]/p/span/text()").extract()[0]
            
            i.add_value(u"label", label)
            i.add_value(u"code", code)
            i.add_value(u"enddate", enddate)
            
            items.append(i.load_item())
        
        if not items:
            spans = hxs.select('//span[@class="content"]/text()')
            for span in spans:
                content = span.extract()
                if not content.strip():
                    continue
                contents = content.split()
                i = XzqhdmItemLoader(XzqhdmItem())
                
                try:
                    i.add_value(u"label", contents[1])
                    i.add_value(u"code", contents[0])
                    i.add_value(u"enddate", enddate)
                except IndexError as ie:
                    print title, content, req_url, 1
#                    raise ie
                except ValueError as ve:
                    print title, content, contents[0], req_url, 2
                
                items.append(i.load_item())
        
        if not items:
            spans = hxs.select('//span[@class="content"]/p/text()')
            for span in spans:
                content = span.extract()
                if not content.strip():
                    continue
                contents = content.split()
                i = XzqhdmItemLoader(XzqhdmItem())
                
                try:
                    i.add_value(u"label", contents[1])
                    i.add_value(u"code", contents[0])
                    i.add_value(u"enddate", enddate)
                    int(contents[0])
                except IndexError as ie:
                    print title, content, req_url, 3
                except ValueError as ve:
                    print title, content, contents[0], req_url, 4
                    
                items.append(i.load_item())
                
        if not items:
            
            if req_url == u'http://www.stats.gov.cn/tjbz/xzqhdm/t20070411_402397928.htm':
                print u'*' * 50
            
            spans = hxs.select('//span[@class="content"]/p//span//text()')
            contents = []
            for span in spans:
                content = span.extract()
                content = content.strip().replace(' ', "").replace('\t', '').replace('\n', '')
                if not content:
                    continue
                else:
                    contents.append(content)
            
#            contents = list(itertools.dropwhile(lambda x: all([str(i) in string.digits for i in x]), contents))
            contents = contents[::-1]
            while contents:
                i = XzqhdmItemLoader(XzqhdmItem())
                code = contents.pop()
                try:
                    int(code)
                    i.add_value(u'code', code)
                    label = contents.pop()
                    i.add_value(u'label', label)
                    i.add_value(u"enddate", enddate)
                    items.append(i.load_item())
                except ValueError as ve:
                    print title, code , req_url
                
        if not items:
            print title, 'fail', req_url, 7
            
        jli_exp = JsonLinesItemExporter(open(enddate + u"/" + title, 'wb'), encoding=u'utf-8')
        for item in items:
            jli_exp.export_item(item)
        
        if items:
            print title, 'done', 8
        
        
        return items
        
#        print response.
#        print response.body.decode('gb2312')
        
        
